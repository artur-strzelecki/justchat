from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SerializersPublicMessage, SerializersRoom
from .models import PublicMessage, Room


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

@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = SerializersRoom(rooms, many=True)
    return Response(serializer.data)

''' END API '''

