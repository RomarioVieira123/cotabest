from django.contrib import admin
from purchase.models import Purchase


class PurchasesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Purchase, PurchasesAdmin)
