from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Creamos las funciones para request - response, con la lógica de negocio.

def index(request):
    products = Product.objects.all()
    return render(request, "../templates/list_of_products.html", {"products": products})