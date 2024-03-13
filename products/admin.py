from django.contrib import admin

# Importamos las clases y las registramos.
from .models import Product

admin.site.register(Product)
