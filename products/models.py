from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=50, null =True)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    brand = models.ForeignKey(
        "products.Brand",
        on_delete=models.CASCADE,
        related_name="products"
    )
    
    image = models.ImageField(
        blank=True, null=True, 
        upload_to="media/products"
        )
    
    discount = models.IntegerField()
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    
    # Definimos el __str__ para que se muestre correctamente el nombre del producto en el panel de administracion.
    def __str__(self):
        return f"{self.name} | {self.brand}"
    
    
class Brand(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    #discount = models.IntegerField()
    
    logo = models.ImageField(
        blank=True, null=True, 
        upload_to="media/brands"
        )
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name