from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from datetime import datetime
from .models import Room,Messages
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
# Create your views here.
def createRoom(user,receiver):
    print(user)
    print(receiver)
    number=Room.objects.all().count()
    time=datetime.now()
    room_name=f"{user}{receiver}"

    print(room_name)
    return room_name
@login_required
def getMessage(request):
    if request.method == 'POST':
        user = request.user
        receiver_id = request.POST.get('id')

        user_receiver = get_object_or_404(User, id=receiver_id)
        room = createRoom(user.id, user_receiver.id)

        try:
            # Try to get the room where the current user is the sender
            room = Room.objects.get(name=room)
        except Room.DoesNotExist:
            try:
                # Try to get the room where the current user is the receiver
                room = Room.objects.get(name=createRoom(user_receiver.id, user.id))
                print(room)
            except Room.DoesNotExist:
                # If the room doesn't exist, create it
                room = Room.objects.create(name=room, sender=user, reciever=user_receiver)

        messages = Messages.objects.filter(Room=room)
        serialized_messages = serialize('json', messages)

        return HttpResponse(serialized_messages, content_type='application/json')

            

        
        

    return HttpResponse('receiver')
@login_required
def Send(request):
    if request.method=='POST':
        user=request.user
        message=request.POST['message']
        receiver=request.POST['reciever_id']
        receiver_obj=User.objects.get(id=receiver)
        room=createRoom(user.id,receiver_obj.id)
        print(user.username,message,receiver_obj.id,room)
        try:
            room_1=Room.objects.get(name=room)
            if room_1 is not None:
                create_message=Messages.objects.create(message=message,sender=user,reciever=receiver_obj,Room=room_1)
        except Room.DoesNotExist:
            room_2=Room.objects.get(name=createRoom(receiver_obj.id,user.id))
            if room_2 is not None:
                create_message=Messages.objects.create(message=message,sender=user,reciever=receiver_obj,Room=room_2)
        
        
        return HttpResponse({message})
def getMessageOfRoom(request):
    if request.method=='POST':
        room_name=request.POST.get('room_name')
        try:
            room=Room.objects.get(name=room_name)
            messages=Messages.objects.filter(Room=room)
            serialized_message=serialize('json',messages)
            return HttpResponse(serialized_message,content_type='application/json')
        except Room.DoesNotExist:
            return HttpResponse('no Room Found')
def getCurrentRoom(request):
    if request.method=='POST':
        user=request.user
        receiver=request.POST['receiver_id']
        room=createRoom(user.id,receiver)
        try:
            get_room=Room.objects.get(name=room)
        except Room.DoesNotExist:
            pass
        try:
            room1=createRoom(receiver,user.id)
            get_room=Room.objects.get(name=room1)
        
        except Room.DoesNotExist:
           pass 
            
            

        return HttpResponse(get_room)