from django.shortcuts import render,redirect
from .models import Courses,Blog
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Auth.models import Course,Students,Parents
from Academics.models import Lessons,Lectures,Internships,RegisteredInterns
from datetime import datetime
from django.db.models import Q
from Academics.models import FAQ
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Create your views here.
def get_time_of_day():
    
    current_hour = datetime.now().hour

    
    morning_threshold = 6 
    afternoon_threshold = 12  
    evening_threshold = 18  

    if current_hour < morning_threshold:
        return "night"
    elif current_hour < afternoon_threshold:
        return "morning"
    elif current_hour < evening_threshold:
        return "afternoon"
    else:
        return "evening"
def Home(request):
    courses=Course.objects.all()
    faq=FAQ.objects.all()
    blog=Blog.objects.all()
    if request.user.is_authenticated:
        try:
            student=Students.objects.get(student=request.user)
            status='student'
        except Students.DoesNotExist:
            try:
                Parents.objects.get(parent=request.user)
                status='parent'
            except Parents.DoesNotExist:
                status='lecture'
    else:
        status=''   
    context={'courses':courses,'faqs':faq,'blogs':blog,'status':status}
    
    return render(request,'home.html',context)
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('home'))
@login_required
def Dashboard(request):
    return render(request,'Dashboard/dashboard.html')
@login_required
def Student_Dashboard(request):
    user=request.user
    try:
       student=Students.objects.get(student=user)
       course=student.course
       lessons=Lessons.objects.filter(course=course)
       parent=Parents.objects.filter(student=student)
       if len(parent)==0:
            message='No appropriate parent'
       else:
            message=''
       date=datetime.now()
       time=get_time_of_day()
    except Students.DoesNotExist:
         return HttpResponseRedirect(reverse('home')) 
        
    context={'lessons':lessons,'date':date,'time':time,'course':course,'message':message}
    return render(request,'Dashboard/studentDashboard.html',context)
@login_required
def Staff_Dashboard(request):
    user = request.user

    try:
        is_lecture = Lectures.objects.get(user=user)
        is_staff = True
    except Lectures.DoesNotExist:
        is_staff = False

    if is_staff:
        return render(request, 'StaffDashboard/staff_dashboard.html', {'is_staff': is_staff})
    else:
        return HttpResponseRedirect(reverse('home')) 
@login_required
def all_parents(request):
    parents=Parents.objects.all()
    context={'parents':parents}
    if request.method=='POST':
        parent_id=request.POST['parent_id']
        parent=Parents.objects.get(id=parent_id)
        parent.student=Students.objects.get(student=request.user)
        parent.save()
        return HttpResponse('success')
    return render(request,'Dashboard/parents.html',context)
@login_required
def InternshipView(request):
    today=datetime.now().date()

    internships=Internships.objects.filter(starting__gt=today)
    try:
        Parents.objects.get(parent=request.user)
        is_staff=True
    except Parents.DoesNotExist:
        is_staff=False
    context={'internships':internships,'is_staff':is_staff}
    return render(request,'Dashboard/internships.html',context)
@login_required
def applyInternship(request):
    if request.method=='POST':
        internship_id=request.POST['internship_id']
        internship_obj=Internships.objects.get(id=internship_id)
        try:
            is_student=Students.objects.get(student=request.user)
            try:
                check=RegisteredInterns.objects.get(Q(student=request.user) & Q(internship=internship_obj))
                message='Already Applied'
            except RegisteredInterns.DoesNotExist:
                message='Registered'
                RegisteredInterns.objects.create(internship=internship_obj,student=request.user)

        except Students.DoesNotExist:
            message='Only students are Allowed to apply'
        context={'message':message}
        return HttpResponse(message)
@login_required
def ParentDashboard(request):
    date=datetime.now()
    time=get_time_of_day()
    try:
        parent=Parents.objects.get(parent=request.user)
        if parent.student is not None:
            message=''
        else:
            message='You have no Student in our system Please Talk to administrator or Your Child to get access on his/her Academic details'
        context={'is_parent':True,'message':message,'date':date,'time':time}
        return render(request,'Dashboard/parent_dashboard.html',context)
    except Parents.DoesNotExist:
        return HttpResponseRedirect(reverse('home'))                 
def ContactUs(request):
    if request.method=='POST':
        sender=request.POST['email']
        message=request.POST['message']
        
        subject=f'School Web Support - Sender {sender}'
        to_email='ngogainnocent1@gmail.com'
        html_content=render_to_string('email.html',{'message':message})
        email = EmailMessage(subject, html_content, sender, [to_email])
        email.content_subtype = 'html' 
        try:
            send=email.send()
            response='Email sent Success'
        except Exception as e:
            response=f'Failed to Send your Email: {str(e)}' 

        return HttpResponse(response)

def SingleBlog(request,id):
    blog=Blog.objects.get(pk=id)
    otherblogs=Blog.objects.exclude(id=id).order_by('-created_at')[:10]
    context={'blog':blog,'otherblogs':otherblogs}
    return render(request,'blog.html',context)
