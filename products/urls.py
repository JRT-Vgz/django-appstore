from django.contrib import admin
from django.urls import path

#Importamos las funciones que vamos a pasar a los paths.
from .views import index

urlpatterns = [
    path('', index),
]