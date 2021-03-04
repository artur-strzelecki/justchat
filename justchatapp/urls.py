from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_view, name='rooms'),
    path('<str:room_name>/', views.chat_view, name='chat'),
    path('api/get_room_messages/<int:pk_room>/', views.get_room_messages, name='get_room_messages'),
    path('api/create_room_message/', views.create_room_messages, name='create_room_message'),
    path('api/get_rooms/', views.get_rooms, name='get_rooms')
]