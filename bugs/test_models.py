from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bug, Comment


class TestBugModel(TestCase):

    def test_description_is_False(self):
        bug = Bug.objects.create(title="")
        bug.save()
        self.assertFalse(bug.title)

    def test_description_is_False(self):
        bug = Bug.objects.create(title="Create a Test")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertFalse(bug.description)

    def test_title_and_description_is_true(self):
        bug = Bug.objects.create(
            title="Create a Test",
            description="Test description")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertTrue(bug.description)

    def test_bug_name(self):
        bug = Bug.objects.create(title="My name is")
        self.assertEqual(str(bug), "My name is")


class TestCommentModel(TestCase):

    def test_comment_as_a_string(self):
        user = User.objects.create_user(
            username='username',
            password='password')
        bug = Bug(
            title="Test bug comment",
            author=user,
            description="Test desc")
        bug.save()
        comment = Comment(context="Test Comment", author=user, bug=bug)
        self.assertEqual(str(comment), 'Test bug comment-username')
