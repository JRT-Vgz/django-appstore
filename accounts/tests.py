from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest import skip


class SignupViewTestCase(TestCase):    
    def setUp(self):
        self.valid_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "testpassword123",
        }
        self.bad_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "otherpassword",
        }
        
    def test_signup_succesful(self):
        response = self.client.post(reverse("signup"), self.valid_data)
        self.assertRedirects(response, reverse("index"))
        self.assertTrue(User.objects.filter(username="testuser").exists())
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(User.objects.get(username="testuser").password, self.valid_data["password1"])
        
    def test_signup_invalid(self):
        response = self.client.post(reverse("signup"), self.bad_data)
        msg = "<li>The two password fields didn\\xe2\\x80\\x99t match.</li>"
        self.assertFalse(User.objects.filter(username="testuser").exists())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(msg in str(response.content))
        self.assertTemplateUsed(response, "accounts/signup.html")
        
                          
class LoginViewTests(TestCase):
    def setUp(self):        
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123'}
        self.user = User.objects.create_user(**self.user_data)
    
        
    def test_login_succesful(self):        
        response = self.client.post(reverse("login"), self.user_data)
        self.assertRedirects(response, reverse("index"))
        self.assertEqual(response.status_code, 302)
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
   
   
    def test_login_invalid(self):
        data = {
            "username": self.user.username,
            "password": "incorrectpassword",
        }
        
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, 200)
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)
        self.assertTemplateUsed(response, "accounts/login.html")
        
        
        