from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import Parents,Students,Marks
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login,authenticate,logout
from Academics.models import Course
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import render_to_string,get_template
# Create your views here.

def createRegNo(course):
    number_of_students=Course.objects.filter(name=course).count()
    course_name=get_object_or_404(Course,pk=course)
    abrev=course_name.name[:3].upper()
    st_no=number_of_students+1
    regNo=f"{abrev}-{st_no}"
    return regNo

def Register(request):
    courses=Course.objects.all()
    if request.method == "POST":
        # Retrieve form data
        username=request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        account_type = request.POST.get('account_type')
        course=request.POST.get('course')
        
        if not (first_name and last_name and email and password and confirm_password and account_type):
            
            return render(request, 'register.html', {'error': 'All fields are required','courses':courses})

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match','courses':courses})
        try:
            validate_password(password, user=request.user)
            hashed_password = make_password(password)
            if User.objects.filter(email=email).exists():
                return render(request,'register.html',{'error':'User with this email Already Registered','courses':courses})
            # Create user
            user = User.objects.create_user(
            username=username,  # Use email as username
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password
            )

            if account_type=='Parent':
                parent=Parents.objects.create(parent=user)
                login(request,user)
                return redirect('staff_dashboard')
            elif account_type=='Student':
                regNo=createRegNo(course)
                course_obj=get_object_or_404(Course,pk=course)
                student=Students.objects.create(student=user,regNo=regNo,course=course_obj)
                login(request,user)
                return redirect('student_dashboard')
                
            else:
                return render(request,'register.html',{'error':'Please choose account','courses':courses})
        except ValidationError as e:
            
            return render(request, 'register.html',{'error':" ".join(e),'courses':courses})
        # Hash the password
       
    else: 
    
       
        context={'courses':courses}
        return render(request,'./register.html',context)
def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email,password)
        user = User.objects.filter(email=email).first()
        if user is not None:
            checkpass=check_password(password,user.password)
            if checkpass:
                student=Students.objects.filter(student=user).first()
                if student:
                    login(request,user)
                    return redirect('student_dashboard') 
                elif not student:
                    
                    parent=Parents.objects.filter(parent=user).first()
                    if parent:
                        login(request,user)
                        
                        return redirect('parent_dashboard')
                    else:
                        login(request,user)
                        
                        return redirect('home')
                else:
                    return redirect(request,'login.html',{'error':'not either parent or student'})
            else:
                return render(request,'login.html',{'error':'Incorect password'})
        else:
            return render(request,'login.html',{'error':'User with this email not found'})
    return render(request, 'login.html')

def getMark(request):
    
    try:
        student=Students.objects.get(student=request.user)
        
        is_parent=False
        student_details=tudent_details=User.objects.get(pk=student.student.id)
    except Students.DoesNotExist:
        try:
            parent=Parents.objects.get(parent=request.user)
            student=Students.objects.get(pk=parent.student)
            student_details=User.objects.get(pk=student.student.id)
            
            is_parent=True
        except Parents.DoesNotExist:
            logout(request)
            return render(request,'login.html',{'message':'Please Login as Student or Parent'})
    marks=Marks.objects.filter(student=student)
    
    context={'marks':marks,'user':request.user,'is_parent':is_parent,'student':student_details,}
    return render(request,'Marks/student_marks.html',context)
    #return render(request,'Marks/downloadable_marks.html',context)

def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

@login_required
def DownloadMarks(request):
    user=request.user
    try:
        student=Students.objects.get(student=request.user)
        is_parent=False
    except Students.DoesNotExist:
        try:
            parent=Parents.objects.get(parent=request.user)
            student=parent.student
            is_parent=True
        except Parents.DoesNotExist:
            return render(request,'login.html',{'message':'Please login as Student or Parent'})
    
    marks=Marks.objects.filter(student=student)
    context={'marks':marks,'user':user,'student':student,'is_parent':is_parent}
    pdf=render_to_pdf('Marks/downloadable_marks.html',context)
    return HttpResponse(pdf,content_type='application/pdf')