
from django.test import TestCase, Client
from django.urls import reverse
from .models import Shop, Discount
from datetime import date, timedelta

class ShopModelTest(TestCase):
    def test_create_shop(self):
        shop = Shop.objects.create(name="Test Shop", address="123 Main St")
        self.assertEqual(str(shop), "Test Shop")
        self.assertEqual(shop.address, "123 Main St")

class DiscountModelTest(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(name="Test Shop", address="123 Main St")

    def test_create_discount(self):
        discount = Discount.objects.create(
            shop=self.shop,
            title="Test Discount",
            description="Save big!",
            amount=10,
            is_percentage=True,
            is_featured=True,
            category="food",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=7)
        )
        self.assertEqual(str(discount), "Test Discount (Test Shop)")
        self.assertTrue(discount.is_featured)
        self.assertEqual(discount.category, "food")

class HomeViewTest(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(name="Test Shop", address="123 Main St")
        Discount.objects.create(
            shop=self.shop,
            title="Featured Discount",
            description="Featured!",
            amount=20,
            is_percentage=True,
            is_featured=True,
            category="fashion",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5)
        )

    def test_homepage_loads(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Featured Discount")
