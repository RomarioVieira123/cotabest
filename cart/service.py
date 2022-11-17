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
    def select_cart_serialized_by_user(cls, request, pk):
        cart = DatabaseCartRepository.select_cart_by_user(request, pk)
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
    def delete_cart_not_serialized(cls, request, pk):

        cart = DatabaseCartRepository.select_cart_by_user(request, pk)
        cart_serializer = CartSerializer(cart)

        DatabaseCartRepository.delete_cart(cart_serializer)

        return None



    @classmethod
    def update_cart_serialized(cls, request):
        products = []

        get_cart = None

        for prod in request.data:
            product = DatabaseProductRepository.select_product(request, prod['product_id'])

            if (int(prod['quantity']) * product.amount_per_package) < product.minimun:
                raise Exception(f'{product.name}{", "}{"Quantity requested: "}{prod["quantity"]}{" below the minimum quantity: "}{product.minimun}{"."}{" Quantity per pack: "}{product.amount_per_package}')
            else:
                products.append(product)

        cart = DatabaseCartRepository.select_cart_by_user(request, request.user.id)
        cart_serializer = CartSerializer(cart)


        if cart is None:
            raise Exception("Cart not found!")
        else:
            get_cart = DatabaseCartRepository.update(request, products, cart, cart_serializer)

        cart_serializer = CartSerializer(get_cart)

        return cart_serializer.data


    @classmethod
    def insert_cart_serialized(cls, request):
        products = []

        get_cart = None

        for prod in request.data:
            product = DatabaseProductRepository.select_product(request, prod['product_id'])

            if (int(prod['quantity']) * product.amount_per_package) < product.minimun:
                raise Exception(f'{product.name}{", "}{"Quantity requested: "}{prod["quantity"]}{" below the minimum quantity: "}{product.minimun}{"."}{" Quantity per pack: "}{product.amount_per_package}')
            else:
                products.append(product)

        cart = DatabaseCartRepository.select_cart_by_user(request, request.user.id)

        if cart is None:
            get_cart = DatabaseCartRepository.save(request, products)
        else:
            raise Exception("There is already a shopping cart open for the user")

        cart_serializer = CartSerializer(get_cart)

        return cart_serializer.data




