from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request, "index.html")


def room(request,room):
    username = request.GET.get('username')
    room_detail = Room.objects.get(name=room)
    return render(request, 'room.html',{'room':room,'username':username,"room_detail":room_detail})


def checkview(request):
    room = request.POST['room_name']
    user = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+user)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+room+'/?username='+user)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST["room_id"]
    new_message = Message.objects.create(msg=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse("Send successfully")


def getMessages(request,room):
    room_detail = Room.objects.get(name=room)
    messages = Message.objects.filter(room__icontains=room_detail.id)
    return JsonResponse({"messages":list(messages.values())})