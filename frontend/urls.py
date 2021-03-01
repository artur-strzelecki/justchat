from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='room'),
    path('<str:room_name>/', views.index, name='chat'),
]