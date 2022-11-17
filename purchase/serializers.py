from rest_framework import serializers
from cart.models import Item
from product.serializers import ProductItemPurchaseSerializer
from purchase.models import Purchase


class PurchaseItemSerializer(serializers.ModelSerializer):
    product = ProductItemPurchaseSerializer()

    class Meta:
        model = Item
        fields = [
            'id',
            'product',
            'quantity',
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    item = PurchaseItemSerializer(many=True)

    class Meta:
        model = Purchase
        fields = [
            'id',
            'total_price',
            'created_at',
            'updated_at',
            'item'
        ]
