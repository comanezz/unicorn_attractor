from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_get_profile_page(self):
        user = User.objects.create_user(
            username='username',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
