from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SerializersPublicMessage
from .models import PublicMessage, Room


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    # check room exists
    room_object = get_object_or_404(Room, name=room_name)

    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


''' API '''
@api_view(['GET'])
def get_room_messages(request, pk_room):
    messages = PublicMessage.objects.filter(room=pk_room).order_by('timestamp')
    serializer = SerializersPublicMessage(messages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_room_messages(request):
    serializer = SerializersPublicMessage(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
''' END API '''

