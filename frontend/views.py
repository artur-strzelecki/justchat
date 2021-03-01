from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from justchatapp.models import Room


def index(request, *args, **kwargs):
    room_name = None

    # if url chat/<str:room_name>
    if len(kwargs) > 0:
        room_name = kwargs['room_name']
        room_obj = get_object_or_404(Room, name=room_name)

    return render(request, 'frontend/index.html', 
                    {'room_name': room_name})
