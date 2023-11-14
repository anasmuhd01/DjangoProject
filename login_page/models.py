from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PRODUCT_TYPE = (
    ("electronics", "Electronics"),
    ("bikes", "Bikes"),
    ("cars", "Cars"),
    ("clothing", "Clothing")
)


STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class ItemModel(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    product_type = models.CharField(max_length=200, choices=PRODUCT_TYPE)

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemModel, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
