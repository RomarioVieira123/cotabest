from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

