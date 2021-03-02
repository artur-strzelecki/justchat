from django.urls import path

from . import views

urlpatterns = [
    path('get_room_messages/<int:pk_room>/', views.get_room_messages, name='get_room_messages'),
    path('create_room_message/', views.create_room_messages, name='create_room_message'),
    path('get_rooms/', views.get_rooms, name='get_rooms')
]