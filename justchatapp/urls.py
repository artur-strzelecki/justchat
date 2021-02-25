from django.urls import path

from . import views

urlpatterns = [
    path('api/get_room_messages/<int:pk_room>/', views.get_room_messages, name='get_room_messages'),
    path('api/create_room_message/', views.create_room_messages, name='create_room_message')
]