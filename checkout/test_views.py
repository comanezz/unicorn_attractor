from django.test import TestCase
from django.contrib.auth.models import User
from features.models import Feature
from django.contrib.messages import get_messages
from checkout.forms import MakePaymentForm, OrderForm


class CheckoutTestViews(TestCase):
    def setUp(self):
        User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_get_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")

    def test_checkout_payment_with_valid_credentials(self):
        feature = Feature(title="Test Feature", description="desc")
        feature.save()

        feature = Feature.objects.get(id=1)
        page = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '8',
            'expiry_year': '2025',
            'stripe_id': 'tok_visa',
        })

        self.assertTrue(page.status_code, 200)

    def test_checkout_payment_with_invalid_credentials(self):
        feature = Feature(title="Test Feature", description="desc")
        feature.save()

        feature = Feature.objects.get(id=1)
        page = self.client.post('/checkout/', {
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '8',
            'expiry_year': '2025',
            'stripe_id': 'tok_chargeDeclined',
        })

        # https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'We were unable to take a payment with that card!')


class CheckoutTestForms(TestCase):

    def test_valid_payment_form(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '12',
            'expiry_year': '2025',
            'stripe_id': 'xyz555',
        })

        self.assertTrue(form.is_valid())

    def test_payment_form_with_missing_field(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'expiry_month': '12',
            'expiry_year': '2099',
        })

        self.assertFalse(form.is_valid())

    def test_valid_order_form(self):
        form = OrderForm({
            "full_name": "Ninho",
            "street_address1": "Hood",
            "street_address2": "Groove Street",
            "town_or_city": "DUBLIN",
            "county": "Dublin",
            "postcode": "01",
            "country": "irlande",
            "phone_number": "0889345739",
        })

        self.assertTrue(form.is_valid())

    def test_order_form_with_missing_field(self):
        form = OrderForm({
            "full_name": "Ninho",
            "street_address1": "Hood",
            "street_address2": "Groove Street",
            "town_or_city": "",
            "county": "Dublin",
            "postcode": "01",
            "country": "irlande",
            "phone_number": "0889345739",
        })

        self.assertFalse(form.is_valid())
