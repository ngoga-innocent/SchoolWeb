from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.
class Courses(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to='course_thumbnail')

    def __str__(self):
        return self.name
class Blog(models.Model):
    title=models.CharField(max_length=255,null=False)
    slug=models.CharField(max_length=255,null=False)
    content=RichTextField()
    thumbnail=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title