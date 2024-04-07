from django.test import TestCase
from django.urls import reverse
from products.models import Product, Comment
from django_dynamic_fixture import G, F
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from unittest import skip


class GetProductViewTestCase(TestCase):
     
    def setUp(self):         
        self.product = G(
            Product,
            name="My Product",
            brand=F(name="My Brand")
        )
               
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/product/" + str(self.product.id))
        self.assertEqual(response.status_code, 200)
            
    def test_view_url_accesible_by_alias(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
               
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertTemplateUsed(response, "products/show_product.html")
        
    def test_view_display_product(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.price)
        self.assertContains(response, self.product.brand.description)
        
        
class GetProductViewLoggedInTestCase(TestCase):
    
    def setUp(self):             
        self.product = G(
            Product,
            name="My Product",
            brand=F(
                name="My Brand",
                description="My Description"),
        )        
        self.comment = G(
            Comment,
            product = self.product,
            text = "My Comment",
            author = "My Author"
            )          
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123'}
        self.user = User.objects.create_user(**self.user_data)        
        self.user.user_permissions.add(Permission.objects.get(codename='view_comment'))        
        self.client.login(username=self.user_data["username"], password=self.user_data["password"])
                
    def test_view_displays_comments(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertContains(response, self.comment.text)
        self.assertContains(response, self.comment.author)
       