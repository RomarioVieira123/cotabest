from rest_framework import serializers

from cart.models import Cart
from product.serializers import ProductSerializer
from user.serializers import ProfileSerializer


class CartSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'open',
            'created_at',
            'updated_at',
            'products',
            'profile'
        ]