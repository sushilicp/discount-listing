from django.db import models
from django.utils import timezone

class Shop(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # In production, use proper password hashing
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Discount(models.Model):
    CATEGORIES = [
        ('Kitchen', 'Kitchen'),
        ('Hotel', 'Hotel'),
        ('Restaurant', 'Restaurant'),
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
    ]
    
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='discounts')
    product_name = models.CharField(max_length=100)
    discount_percentage = models.FloatField()
    category = models.CharField(max_length=50, choices=CATEGORIES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.discount_percentage}%"