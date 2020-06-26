from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class TestUserLoginForm(TestCase):

    def test_login_without_password(self):
        form = UserLoginForm({'username': 'test'})
        self.assertFalse(form.is_valid())

    def test_login_with_username_and_password(self):
        form = UserLoginForm({'username': 'test',
                              'password': "password"})
        self.assertTrue(form.is_valid())

    def test_error_message_for_missing_username(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_error_message_for_missing_password(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):

    def test_register_login_without_required_values(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())

    def test_registration_with_not_same_passwords(self):
        form = UserRegistrationForm({'username': 'test',
                                     'email': 'test@test.com',
                                     'password1': 'password',
                                     'password2': 'not'})
        self.assertFalse(form.is_valid())

    def test_registration_with_required_values(self):
        form = UserRegistrationForm({'username': 'test',
                                     'email': 'test@test.com',
                                     'password1': 'samepassword',
                                     'password2': 'samepassword'})
        self.assertTrue(form.is_valid())
