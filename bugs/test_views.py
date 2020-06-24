
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    def test_get_add_bug_page(self):
        page = self.client.get('/bugs/new')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugform.html")