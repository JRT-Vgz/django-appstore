from django.test import TestCase
from django.urls import reverse
from products.models import Product, Comment
from django_dynamic_fixture import G, F
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from unittest import skip

class IndexViewTestCase(TestCase):
    
    def test_index_view_url_exists_at_desired_location(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
            
    def test_index_view_url_accesible_by_alias(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
          
    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "products/list_of_products.html")


class GetProductViewTestCase(TestCase):
    
    def setUp(self):         
        self.product = G(
            Product,
            name="My Product",
            brand=F(name="My Brand",
                    discount=40)
        )
        self.comment = G(
            Comment,
            product = self.product,
            text = "My Comment",
            author = "My Author"
            )
          
    def test_get_product_view_url_exists_at_desired_location(self):
        response = self.client.get("/product/" + str(self.product.id))
        self.assertEqual(response.status_code, 200)
      
    def test_get_product_view_url_accesible_by_alias(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
         
    def test_get_product_view_uses_correct_template(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertTemplateUsed(response, "products/show_product.html")
  
    def test_get_product_view_display_product(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.price)
        self.assertContains(response, self.product.brand.description)
   
    def test_get_product_view_redirects_to_index_if_product_id_doesnt_exist(self):
        response = self.client.get(reverse("get_product", args=["incorrectID"]))
        self.assertEqual(response.status_code, 302)
 
    def test_get_product_view_hides_comments(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertNotContains(response, self.comment.text)
        self.assertNotContains(response, self.comment.author)
        
        
class GetProductViewLoggedInTestCase(TestCase):
    
    def setUp(self):             
        self.product = G(
            Product,
            name="My Product",
            brand=F(
                name="My Brand",
                description="My Description",
                discount=40)
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
           
    def test_get_product_view_displays_comments(self):
        response = self.client.get(reverse("get_product", args=[self.product.id]))
        self.assertContains(response, self.comment.text)
        self.assertContains(response, self.comment.author)
        
        
class AddNewCommentViewTestCase(TestCase):
    
    def setUp(self):
                 
        self.product = G(
            Product,
            name="My Product",
            brand=F(name="My Brand"),
        )

    def test_add_comment_view_url_exists_at_desired_location(self):
        response = self.client.post("/product/" + str(self.product.id) + "/add_new_comment")
        self.assertEqual(response.status_code, 302)
     
    def test_add_comment_view_url_accesible_by_alias(self):
        response = self.client.post(reverse("add_new_comment", args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

        
       