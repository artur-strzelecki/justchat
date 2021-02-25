from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from justchatapp.models import Room


def index(request):
    return render(request, 'frontend/index.html')


def room(request, room_name):
    # check room exists
    room_object = get_object_or_404(Room, name=room_name)

    return render(request, 'frontend/room.html', {
        'room_name': room_name
    })