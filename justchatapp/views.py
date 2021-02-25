from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SerializersPublicMessage
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
''' END API '''

