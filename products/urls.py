from django.contrib import admin
from django.urls import path

#Importamos las funciones que vamos a pasar a los paths.
from .views import index, get_product

urlpatterns = [
    path('', index),
    path("product/<int:id>", get_product, name="get_product"),
]