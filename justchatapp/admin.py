from django.contrib import admin
from .models import Room, PublicMessage

# Register your models here.
admin.site.register(Room)
admin.site.register(PublicMessage)