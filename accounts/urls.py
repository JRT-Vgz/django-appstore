from django.contrib import admin
from django.urls import path

#Importamos las funciones que vamos a pasar a los paths.
from .views import login_view, logout_view

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
]