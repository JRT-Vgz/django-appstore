from django.contrib import admin

# Importamos las clases y las registramos.
from .models import Product, Brand

admin.site.register(Product)
admin.site.register(Brand)
