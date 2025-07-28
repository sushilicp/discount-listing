from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Shop, Discount
from .forms import ShopForm, DiscountForm
from django.utils import timezone
from datetime import timedelta

def home(request):
    category = request.GET.get('category', '')
    date_filter = request.GET.get('date', '')
    search_query = request.GET.get('search', '')

    discounts = Discount.objects.select_related('shop')
    
    today = timezone.now().date()
    tomorrow = today + timedelta(days=1)
    week_end = today + timedelta(days=7)
    
    if date_filter == 'today':
        discounts = discounts.filter(start_date__lte=today, end_date__gte=today)
    elif date_filter == 'tomorrow':
        discounts = discounts.filter(start_date__lte=tomorrow, end_date__gte=tomorrow)
    elif date_filter == 'week':
        discounts = discounts.filter(start_date__lte=week_end, end_date__gte=today)
    
    if category:
        discounts = discounts.filter(category=category)
    
    if search_query:
        discounts = discounts.filter(
            Q(product_name__icontains=search_query) | Q(shop__name__icontains=search_query)
        )
    
    featured = Discount.objects.filter(is_featured=True)[:3]
    categories = Discount.CATEGORIES
    
    return render(request, 'discount_listing/index.html', {
        'discounts': discounts,
        'featured': featured,
        'categories': categories,
        'selected_category': category,
        'selected_date': date_filter,
        'search_query': search_query,
    })

def signup(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            sentry_sdk.capture_event({
                'message': 'User signed up',
                'level': 'info',
                'extra': {'username': form.cleaned_data['username']}
            })
            return redirect('home')
    else:
        form = ShopForm()
    return render(request, 'discount_listing/signup.html', {'form': form})

def add_discount(request):
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            sentry_sdk.capture_event({
                'message': 'Discount added',
                'level': 'info',
                'extra': {'shop_name': form.cleaned_data['shop'].name}
            })
            return redirect('home')
    else:
        form = DiscountForm(initial={'shop': 1})  # Simplified for demo; use authentication in production
    return render(request, 'discount_listing/add_discount.html', {'form': form})