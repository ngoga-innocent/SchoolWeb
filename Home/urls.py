from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('blog/<int:id>',views.SingleBlog,name='single_blog'),
    path('logout',views.Logout,name='logout'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('student_dashboard',views.Student_Dashboard,name='student_dashboard'),
    path('staff_dashboard',views.Staff_Dashboard,name='staff_dashboard'),
    path('parent_dashboard',views.ParentDashboard,name='parent_dashboard'),
    path('parent',views.all_parents,name='parents'),
    path('internship',views.InternshipView,name='internship'),
    path('apply_internship',views.applyInternship,name='apply_internship'),
    path('contact_us',views.ContactUs,name='contact_us'),

]