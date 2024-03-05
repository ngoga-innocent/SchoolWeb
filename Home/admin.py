from django.contrib import admin
from .models import Courses,Blog
from Academics.models import FAQ
# Register your models here.
admin.site.register(Courses)
admin.site.register(FAQ)
admin.site.register(Blog)