from django.test import TestCase
from .forms import *


class TestFeatureForm(TestCase):
    def test_create_feature_with_only_title(self):
        form = FeatureForm({'title': 'test'})
        self.assertFalse(form.is_valid())

    def test_create_feature_with_only_description(self):
        form = FeatureForm({'description': 'test'})
        self.assertFalse(form.is_valid())

    def test_create_feature_with_title_and_description(self):
        form = FeatureForm({'title': 'test title', 'description': 'test'})
        self.assertTrue(form.is_valid())

    def test_error_message_for_missing_title(self):
        form = FeatureForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

    def test_error_message_for_missing_description(self):
        form = FeatureForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['description'], [u'This field is required.'])


class TestFeatureComment(TestCase):
    def test_create_comment_without_comment(self):
        form = CommentForm({'context': ''})
        self.assertFalse(form.is_valid())

    def test_create_comment_wit_comment(self):
        form = CommentForm({'context': 'test'})
        self.assertTrue(form.is_valid())
