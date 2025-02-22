from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class CategoryChoices(models.TextChoices):
    ELECTRONICS = "ELEC", "Electronics & Gadgets"
    FASHION = "FASH", "Fashion & Apparel"
    HOME = "HOME", "Home & Living"
    BEAUTY = "BEAU", "Beauty & Personal Care"
    HEALTH = "HEAL", "Health & Wellness"
    BOOKS = "BOOK", "Books & Stationery"
    TOYS = "TOYS", "Toys"
    KIDS = "KIDS", "Kids & Baby Products"
    SPORTS = "SPOR", "Sports & Outdoors"
    GROCERIES = "GROC", "Groceries & Food Items"
    AUTOMOTIVE = "AUTO", "Automotive & Tools"
    PET_SUPPLIES = "PET", "Pet Supplies"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField(null=True,blank=True)
    productCategory =  models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.ELECTRONICS
    )
    Rating = models.DecimalField(
        default=0.0,
        max_digits=2,
        decimal_places=1
    )
    Images = ArrayField(models.ImageField(upload_to="product_images/"), blank=True, null=True)