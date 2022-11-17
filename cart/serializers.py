from rest_framework import serializers

from cart.models import Cart, Item
from product.serializers import ProductSerializer
from user.serializers import ProfileSerializer, UserSerializer


class ItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Item
        fields = [
            'id',
            'created_at',
            'updated_at',
            'product',
            'quantity',
        ]


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    item = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'created_at',
            'updated_at',
            'user',
            'quantity',
            'ammount',
            'item'
        ]
