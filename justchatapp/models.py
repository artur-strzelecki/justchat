from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Room(models.Model):
    name = models.TextField(blank=False)
    created = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)


class PublicMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    timestamp = models.DateTimeField(default=datetime.now)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    @staticmethod
    def load_messages(room):
        return PublicMessage.objects.filter(room=room).order_by('-timestamp')

