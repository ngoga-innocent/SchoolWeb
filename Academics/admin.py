from django.contrib import admin
from .models import Course,Lectures,Lessons
# Register your models here.
admin.site.register(Course)
admin.site.register(Lectures)
admin.site.register(Lessons)