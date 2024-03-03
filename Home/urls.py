from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('logout',views.Logout,name='logout'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('student_dashboard',views.Student_Dashboard,name='student_dashboard'),
    path('staff_dashboard',views.Staff_Dashboard,name='staff_dashboard'),
    path('parent',views.all_parents,name='parents'),
    path('internship',views.InternshipView,name='internship'),
    path('apply_internship',views.applyInternship,name='apply_internship')
]