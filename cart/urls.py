from django.urls import path
from .views import AddToCartView, CartDetailView, CheckoutView

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
]
