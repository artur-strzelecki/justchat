from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from justchatapp.views import main_view

urlpatterns = [
    path('', main_view),
    path('chat/', include('justchatapp.urls')),
    path('admin/', admin.site.urls)
]
