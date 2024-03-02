from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Auth.models import Students
from .models import Lectures,Course
from Chat.models import Room
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
@login_required
def getLectures(request):
    user = request.user
    
    try:
        student = Students.objects.get(student=user)
        course = student.course
        lectures = Lectures.objects.filter(course=course)
        context = {'course': course, 'lectures': lectures}
        return render(request, 'lectures.html', context)
    except Students.DoesNotExist:
        pass  
    
    try:
        
        lecture = Lectures.objects.get(user=user)
        
        rooms = Room.objects.filter(Q(sender=lecture.user) | Q(reciever=lecture.user))
        context = {'rooms': rooms}
        return render(request, 'lectures.html', context)
    except Lectures.DoesNotExist:
        return render(request, 'staff_dashboard.html')


    