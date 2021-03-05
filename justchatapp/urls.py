from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_view, name='rooms'),
    path('<str:room_name>/', views.chat_view, name='chat'),
]