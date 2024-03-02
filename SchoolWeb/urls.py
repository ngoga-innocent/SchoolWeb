
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls'),name='Home'),
    path('auth',include('Auth.urls'),name='auth'),
    path('academic',include('Academics.urls'),name='academic'),
    path('chat',include('Chat.urls'),name='chat'),
    path("__reload__/", include("django_browser_reload.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
