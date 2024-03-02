from django.shortcuts import render
from .models import Courses
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Auth.models import Course,Students,Parents
from Academics.models import Lessons,Lectures
from datetime import datetime
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
    date=datetime.now()
    time=get_time_of_day()
    context={'lessons':lessons,'date':date,'time':time,'course':course}
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
    
   