from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    minimun = models.PositiveIntegerField(default=0)
    amount_per_package = models.PositiveIntegerField(default=0)
    max_availability = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name', 'price', 'id')

    def __unicode__(self):
        return self.name
