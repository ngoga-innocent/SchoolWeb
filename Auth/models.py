from django.db import models
from django.contrib.auth.models import User
import uuid
from Academics.models import Course,Lessons
# Create your models here.
class Students(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    regNo=models.CharField(max_length=255,null=False,primary_key=True)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.regNo
    
class Parents(models.Model):
    parent=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    student=models.ForeignKey(Students,on_delete=models.CASCADE,null=True,related_name='my_student')

    


class Marks(models.Model):
    test = 'Test'
    exam = 'Exam'
    assignment = 'Assignment'
    choices=[
        (test,'test'),
        (exam,'exam'),
        (assignment,'Assignment')
    ]
    student=models.ForeignKey(Students,on_delete=models.CASCADE,null=False)
    lesson=models.ForeignKey(Lessons,on_delete=models.CASCADE,null=False)
    marks=models.IntegerField()
    total=models.IntegerField()
    type=models.CharField(max_length=255,choices=choices,null=False,default=assignment)

    
