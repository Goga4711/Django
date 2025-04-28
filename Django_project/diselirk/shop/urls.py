# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница (для http://127.0.0.1:8000/)
    path('product_list/', views.product_list, name='product_list'),  # Страница товаров (для http://127.0.0.1:8000/product_list/)
]
