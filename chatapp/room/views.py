from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . models import Room, Message

# Create your views here.
@login_required
def rooms(request):
    return render(request, 'room/rooms.html', {
        'rooms': Room.objects.all()
    })


@login_required
def room(request, slug):
    return render(request, 'room/room.html', {
        'room': Room.objects.get(slug=slug),
        'messages': Message.objects.filter(room=room)[0:25]
    })