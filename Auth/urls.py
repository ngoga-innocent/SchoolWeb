from django.urls import path
from .import views

urlpatterns = [
    path('',views.Login, name='login'),
    path('register',views.Register,name='register'),
    path('marks',views.getMark,name='marks'),
    path('download',views.DownloadMarks,name='download_marks')
]