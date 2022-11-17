from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from product.models import Product


class PurchaseItem(models.Model):
    product = models.ForeignKey(Product, related_name='product_purchase', blank=False, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='user_purchase', on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    item = models.ManyToManyField(PurchaseItem, related_name='item_purchase')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
