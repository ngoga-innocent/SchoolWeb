from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=255,null=False)
    def __str__(self):
        return self.name
    
class Lessons(models.Model):
    name=models.CharField(max_length=255,null=False)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Lectures(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    #name=models.CharField(max_length=255,null=False)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)

