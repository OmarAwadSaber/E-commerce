from rest_framework import serializers
from order.serializers import OrderSerializer  
from .models import Cart 

class CartSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    total_cart_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta : 
        model = Cart
        fields = ['user', 'created_at', 'orders', 'total_cart_price']