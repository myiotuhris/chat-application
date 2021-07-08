from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
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

def sendMessage(request):
    text=request.POST['message']
    room_id = request.POST['room_id']
    user=request.POST['username']

    new_msg=Message.objects.create(value=text, username= user,room= room_id)
    new_msg.save()
    return HttpResponse("Message Sent!")

def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})