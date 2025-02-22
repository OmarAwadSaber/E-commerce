from django.db import models
from users.models import User
# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    orders = models.ManyToManyField('order.Order', blank=True)
    def total_cart_price(self):
        return sum(order.order_price for order in self.orders.all())
