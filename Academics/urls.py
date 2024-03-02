from django.urls import path
from .import views

urlpatterns = [
    path('',views.getLectures, name='get_lectures'),
    
    
]