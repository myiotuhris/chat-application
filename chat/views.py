from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    return render(request,'room.html',{
        'room': room,
        'username': username,
        'room_details': room_details,
    })

def checkRoom(request):
    room=request.POST['room_name']
    user=request.POST['username']
    if not Room.objects.filter(name=room).exists():
        newroom=Room.objects.create(name=room)
        newroom.save()
    return redirect('/'+room+'/?username='+user)
