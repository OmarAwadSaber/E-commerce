from django.db import models
from products.models import Product
from users.models import User
from cart.models import Cart
# Create your models here.
class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    Amount = models.IntegerField(default=1)

    @property
    def order_price(self):
        return self.Amount * self.product.price