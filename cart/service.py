import json
from django.core import serializers
from cart.database import DatabaseCartRepository
from cart.serializers import CartSerializer
from product.database import DatabaseProductRepository
from user.database import DatabaseUserRepository


class CartService:

    @classmethod
    def select_cart_serialized(cls, request, pk):
        cart = DatabaseCartRepository.select_cart(request, pk)
        cart_serializer = CartSerializer(cart)

        return cart_serializer.data

    @classmethod
    def select_cart_not_serialized(cls, request, pk):
        cart = DatabaseCartRepository.select_cart(request, pk)
        return cart

    @classmethod
    def select_all_carts_serialized(cls):
        carts = DatabaseCartRepository.select_all_carts()
        data = serializers.serialize("json", carts)
        data_json = json.loads(data)

        return data_json

    @classmethod
    def select_all_carts_not_serialized(cls):
        carts = DatabaseCartRepository.select_all_carts()

        return list(carts)

    @classmethod
    def update_cart_serialized(cls, request, pk):
        pass

    @classmethod
    def delete_cart_serialized(cls, request, pk):
        pass

    @classmethod
    def insert_cart_serialized(cls, request):
        products = []

        for prod in request.data:
            product = DatabaseProductRepository.select_product(request, prod['product_id'])

            if (int(prod['quantity']) * product.amount_per_package) < product.minimun:
                raise Exception(f'{product.name}{", "}{"Quantity requested: "}{prod["quantity"]}{" below the minimum quantity: "}{product.minimun}{"."}{" Quantity per pack: "}{product.amount_per_package}')
            else:
                products.append(product)


