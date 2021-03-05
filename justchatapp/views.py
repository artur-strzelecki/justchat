from django.shortcuts import render, redirect, get_object_or_404
from .models import PublicMessage, Room


def rooms_view(request):
    rooms = Room.objects.all()
    return render(request, 'chat/rooms.html', {'rooms': rooms})


def chat_view(request, room_name):
    room_obj = get_object_or_404(Room, name=room_name)

    return render(request, 'chat/chat.html', {'room_name': room_name})

def main_view(request):
    return redirect('rooms')