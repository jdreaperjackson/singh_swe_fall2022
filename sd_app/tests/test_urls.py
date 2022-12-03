from django.test import SimpleTestCase
from django.urls import reverse, resolve
from sd_app.views import profilePage, buyPage, registerPage, purchaseHistoryPage

class TestUrls(SimpleTestCase):

    def test_buypage_url(self):
        url = reverse('sd_app:buy')
        self.assertEquals(resolve(url).func, buyPage)

    def test_profilepage_url(self):
        url = reverse('sd_app:profile')
        self.assertEquals(resolve(url).func, profilePage)

    def test_registerpage_url(self):
        url = reverse('sd_app:register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_purchase_history_page_url(self):
        url = reverse('sd_app:purchase_history')
        self.assertEquals(resolve(url).func, purchaseHistoryPage)