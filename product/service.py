import json
from django.core import serializers
from product.database import DatabaseProductRepository
from product.serializers import ProductSerializer


class ProductService:

    @classmethod
    def search_products_not_serialized(cls, request):
        products = DatabaseProductRepository.search_products(request)

        serializer = ProductSerializer(products, many=True)

        return list(serializer.data)
    
    @classmethod
    def select_product_serialized(cls, request, pk):
        product = DatabaseProductRepository.select_product(request, pk)
        product_serializer = ProductSerializer(product)

        return product_serializer.data

    @classmethod
    def select_product_not_serialized(cls, request, pk):
        product = DatabaseProductRepository.select_product(request, pk)
        return product

    @classmethod
    def select_all_products_serialized(cls):
        products = DatabaseProductRepository.select_all_products()
        data = serializers.serialize("json", products)
        data_json = json.loads(data)

        return data_json

    @classmethod
    def select_all_products_not_serialized(cls):
        products = DatabaseProductRepository.select_all_products()

        return list(products)