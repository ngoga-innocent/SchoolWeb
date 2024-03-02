from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Room(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    reciever=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    name=models.CharField(max_length=255,editable=False,unique=True,primary_key=True)

    def __str__(self):
        return self.name
class Messages(models.Model):
    message=models.TextField()
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_message')
    reciever=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver_message')
    Room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"