from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(default=0.0)
    minimun = models.PositiveIntegerField(default=0)
    amount_per_package = models.PositiveIntegerField(default=0)
    max_availability = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
