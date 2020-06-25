
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_get_add_bug_page(self):
        page = self.client.get('/bugs/new/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugform.html")

    def test_get_edit_bug_page(self):
        user = User.objects.get(username="username")
        bug = Bug.objects.create(title="test", description="testing", author_id=user.id)
        bug.save()

        page = self.client.get('/bugs/{0}/{1}/edit/'.format(bug.id, bug.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugform.html")
    
    def test_get_edit_page_for_bug_that_does_not_exist(self):
        page = self.client.get("/bugs/999/nothing/edit/")
        self.assertEqual(page.status_code, 404)

    def test_get_bugs_list_page(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

    def test_get_bugs_detail_page(self):
        bug = Bug.objects.create(title="test", description="testing")
        bug.save()

        page = self.client.get('/bugs/{0}/{1}/'.format(bug.id, bug.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugdetail.html")