from django.test import TestCase
from products.models import Product, Brand, Comment
from django_dynamic_fixture import G, F


class ProductModelTestCase(TestCase):
       
    def setUp(self):        
        self.product = G(
            Product,
            name="My Product",
            brand=F(name="My Brand"),
        )
        
    def test_product_str_method(self):
        expected_str = f"{self.product.name} | {self.product.brand}"
        self.assertEqual(str(self.product), expected_str)
   
    def test_product_attributes(self):
        self.assertEqual(self.product.name, "My Product")
        self.assertTrue(hasattr(self.product, "price"))
        self.assertTrue(hasattr(self.product, "description"))
        self.assertTrue(hasattr(self.product, "sku"))
        self.assertTrue(hasattr(self.product, "category"))
        self.assertEqual(self.product.brand.name, "My Brand")
        self.assertTrue(hasattr(self.product, "discount"))
        self.assertTrue(hasattr(self.product, "created_date"))
        self.assertTrue(hasattr(self.product, "published_date"))
    

class BrandModelTestCase(TestCase):
    
    def setUp(self):
        self.brand = G(
            Brand,
            name = "My Brand",
        )
        
    def test_brand_str_method(self):
        self.assertEqual(str(self.brand), self.brand.name)
        
    def test_brand_attributes(self):
        self.assertEqual(self.brand.name,"My Brand")
        self.assertTrue(hasattr(self.brand,"description"))
        self.assertTrue(hasattr(self.brand,"logo"))
        self.assertIsNotNone(self.brand.created_date)
        self.assertTrue(hasattr(self.brand,"published_date"))
        
           
class CommentModelTestCase(TestCase):
    
    def setUp(self):
        self.product = G(
            Product,
            name="My Product",
            brand=F(name="My Brand"),
        )
        
        self.comment = G(
            Comment,
            product = self.product,
            text = "My Comment"
            )
    
    def test_comment_str_method(self):
        self.assertEqual(str(self.comment), self.comment.text)
    
    def test_comment_attributes(self):
        self.assertEqual(self.comment.product.name,"My Product")
        self.assertTrue(hasattr(self.comment,"author"))
        self.assertEqual(self.comment.text, "My Comment")
        self.assertIsNotNone(self.comment.created_date)
        self.assertIsNotNone(self.comment.approved_comment)
                     
    def test_approve_method(self):
        self.assertFalse(self.comment.approved_comment)
        self.comment.approve()
        self.assertTrue(self.comment.approved_comment)