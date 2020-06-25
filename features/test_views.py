
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_get_add_feature_page(self):
        page = self.client.get('/features/new/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureform.html")

    def test_get_edit_feature_page(self):
        user = User.objects.get(username="username")
        feature = Feature.objects.create(title="test", description="testing", author_id=user.id)
        feature.save()

        page = self.client.get('/features/{0}/{1}/edit/'.format(feature.id, feature.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureform.html")
    
    def test_get_edit_page_for_feature_that_does_not_exist(self):
        page = self.client.get("/features/999/nothing/edit/")
        self.assertEqual(page.status_code, 404)

    def test_get_features_list_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")

    def test_get_features_detail_page(self):
        feature = Feature.objects.create(title="test", description="testing")
        feature.save()

        page = self.client.get('/features/{0}/{1}/'.format(feature.id, feature.slug))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featuredetail.html")