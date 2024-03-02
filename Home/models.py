from django.db import models
import uuid
# Create your models here.
class Courses(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to='course_thumbnail')

    def __str__(self):
        return self.name