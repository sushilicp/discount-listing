
from django.db import models

# Basic Shop model for Discount-Listing app
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Basic Discount model for Discount-Listing app
class Discount(models.Model):
    CATEGORIES = [
        ("food", "Food & Beverage"),
        ("fashion", "Fashion"),
        ("electronics", "Electronics"),
        ("health", "Health & Beauty"),
        ("home", "Home & Living"),
        ("other", "Other"),
    ]

    category = models.CharField(max_length=30, choices=CATEGORIES, default="other")
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, related_name='discounts')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_percentage = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.shop.name})"
