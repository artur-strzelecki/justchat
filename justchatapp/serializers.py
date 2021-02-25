from .models import PublicMessage, Room
from rest_framework import serializers


class SerializersPublicMessage(serializers.ModelSerializer):
    class Meta:
        model = PublicMessage
        fields = '__all__'
