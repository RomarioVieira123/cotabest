from rest_framework import serializers
from product.models import Product
from user.serializers import ProfileSerializer


class ProductSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'minimun',
            'amount_per_package',
            'max_availability',
            'profile'
        ]