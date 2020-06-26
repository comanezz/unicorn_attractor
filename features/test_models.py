from django.test import TestCase
from django.contrib.auth.models import User
from .models import Feature, Comment


class TestFeatureModel(TestCase):

    def test_description_is_False(self):
        feature = Feature.objects.create(title="")
        feature.save()
        self.assertFalse(feature.title)

    def test_description_is_False(self):
        feature = Feature.objects.create(title="Create a Test")
        feature.save()
        self.assertEqual(feature.title, "Create a Test")
        self.assertFalse(feature.description)

    def test_title_and_description_is_true(self):
        feature = Feature.objects.create(
            title="Create a Test",
            description="Test description")
        feature.save()
        self.assertEqual(feature.title, "Create a Test")
        self.assertTrue(feature.description)

    def test_feature_name(self):
        feature = Feature.objects.create(title="My name is")
        self.assertEqual(str(feature), "My name is")


class TestCommentModel(TestCase):

    def test_comment_as_a_string(self):
        user = User.objects.create_user(
            username='username', password='password')
        feature = Feature(
            title="Test feature comment", author=user, description="Test desc")
        feature.save()
        comment = Comment(
            context="Test Comment", author=user, feature=feature)
        self.assertEqual(str(comment), 'Test feature comment-username')
