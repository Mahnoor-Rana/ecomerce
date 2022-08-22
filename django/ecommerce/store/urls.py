from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = 'store'),
    path('cart/', views.cart, name = 'cart'),
    path('main/', views.main, name = 'main'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('update_item/', views.updateItem, name = 'update_item'),
]
