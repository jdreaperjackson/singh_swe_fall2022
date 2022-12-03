
from urllib import response
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from sd_app.views import profilePage, buyPage, registerPage, purchaseHistoryPage
from sd_app.models import UserProfile, Transaction
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(
        username="New_user", email="New_user@user.com", password="12345")

    def test_profilepage_GET(self):
        response = self.client.get(reverse('sd_app:profile'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'sd_app/profile.html')
    
    def test_buypage_GET(self):
        response = self.client.get(reverse('sd_app:buy'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'sd_app/buy.html')
    
    def test_registerpage_GET(self):
        response = self.client.get(reverse('sd_app:register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
    
    def test_create_user(self):
        new_user = self.user
        self.assertEqual(new_user.username, "New_user")
        self.assertEqual(new_user.email, "New_user@user.com")

    def test_purchase_history_page_GET(self):
        response = self.client.get(reverse('sd_app:purchase_history'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'sd_app/purchase_hisotry.html')


    
    
