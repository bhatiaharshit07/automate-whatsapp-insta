from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_whatsapp, name='home_whatsapp'),
    path('result/', views.result, name="result"),
]