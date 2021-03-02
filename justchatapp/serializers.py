from .models import PublicMessage, Room
from rest_framework import serializers


class SerializersPublicMessage(serializers.ModelSerializer):
    class Meta:
        model = PublicMessage
        fields = '__all__'

class SerializersRoom(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
