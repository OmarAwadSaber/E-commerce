from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer
from users.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()
    order_price = serializers.ReadOnlyField()
    class Meta :
        model = Order
        fields = '__all__'
