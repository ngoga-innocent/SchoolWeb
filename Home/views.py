from django.shortcuts import render,redirect
from .models import Courses
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Auth.models import Course,Students,Parents
from Academics.models import Lessons,Lectures,Internships,RegisteredInterns
from datetime import datetime
from django.db.models import Q
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
    courses=Courses.objects.all()
    context={'courses':courses}
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
    student=Students.objects.filter(student=user).first()
    course=student.course
    lessons=Lessons.objects.filter(course=course)
    parent=Parents.objects.filter(student=student)
    if len(parent)==0:
        message='No appropriate parent'
    else:
        message=''
    date=datetime.now()
    time=get_time_of_day()
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
    context={'internships':internships}
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
                 
   