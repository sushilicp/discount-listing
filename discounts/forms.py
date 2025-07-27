from django import forms
from .models import Shop, Discount

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'address']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['shop', 'title', 'description', 'amount', 'is_percentage', 'category', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
