from django.test import TestCase
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        
    def test_get_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")