# shop/views.py
from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'shop/index.html')  # Главная страница (index.html)

def product_list(request):
    products = Product.objects.all()  # Загружаем все товары из базы данных
    return render(request, 'shop/product_list.html', {'products': products})
