from django.contrib import admin
from .models import Course,Lectures,Lessons,Internships,RegisteredInterns
# Register your models here.
admin.site.register(Course)
admin.site.register(Lectures)
admin.site.register(Lessons)
admin.site.register(Internships)
admin.site.register(RegisteredInterns)