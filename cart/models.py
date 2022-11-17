from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from product.models import Product


class Item(models.Model):
    product = models.ForeignKey(Product, related_name='product', blank=False, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, related_name='item')
    quantity = models.PositiveIntegerField(default=0)
    ammount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

