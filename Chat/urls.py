from django.urls import path
from .import views

urlpatterns = [
    path('',views.getMessage, name='chat'),
    path('send_chat',views.Send,name='send_chat'),
    path('get_current_room',views.getCurrentRoom,name='get_current_room'),
    path('get_room_messages',views.getMessageOfRoom,name='get_room_messages'),
   
]