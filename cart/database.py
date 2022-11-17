from django.db import transaction
from cart.models import Cart, Item
from product.database import DatabaseProductRepository
from product.service import ProductService


class DatabaseCartRepository:

    @classmethod
    def select_cart(cls, request, pk):
        cart = Cart.objects.filter(id=pk).first()
        return cart

    @classmethod
    def select_item(cls, pk):
        item = Item.objects.filter(id=pk).first()
        return item

    @classmethod
    def select_all_carts(cls):
        carts = Cart.objects.filter().all()
        return carts

    @classmethod
    def select_cart_by_user(cls, request, pk):
        cart = Cart.objects.filter(user__id=pk).first()
        return cart


    @classmethod
    @transaction.atomic()
    def delete_cart(cls, request, cart_serialized):
        cart = Cart.objects.filter(id=cart_serialized.data['id']).first()

        for i in cart_serialized.data['item']:
            product = ProductService.select_product_not_serialized(request, i['product']['id'])
            product.max_availability = product.max_availability + i['quantity']
            product.save()

            item = cls.select_item(i['id'])
            item.delete()

        cart.delete()

        return None

    @classmethod
    @transaction.atomic
    def save(cls, request):

        ammount = 0
        quantity = 0

        for p in request.data:
            product = ProductService.select_product_not_serialized(request, p['product_id'] )
            ammount = ammount + (product.price * int(p['quantity']))

        for p in request.data:
            quantity = quantity + int(p['quantity'])

        itens = []

        for p in request.data:
            product = DatabaseProductRepository.select_product(request, p['product_id'])
            item = Item.objects.create(
                product=product,
                quantity=int(p['quantity'])
            )
            itens.append(item)

        cart = Cart.objects.create(
            user=request.user,
            ammount=ammount,
            quantity=quantity
        )

        for i in itens:
            cart.item.add(i)

        for p in request.data:
            product = ProductService.select_product_not_serialized(request, p['product_id'])
            product.max_availability = product.max_availability - int(p['quantity'])
            product.save()

        return cart

    @classmethod
    @transaction.atomic
    def update(cls, request, cart, cart_serializer):

        ammount = 0
        quantity = 0

        for p in request.data:
            product = ProductService.select_product_not_serialized(request, p['product_id'] )
            ammount = ammount + (product.price * int(p['quantity']))


        for p in request.data:
            quantity = quantity + int(p['quantity'])

        itens = []

        for i in cart_serializer.data['item']:
            item = DatabaseCartRepository.select_item(i['id'])
            item.delete()

        for p in request.data:
            product = DatabaseProductRepository.select_product(request, p['product_id'])
            item = Item.objects.create(
                product=product,
                quantity=int(p['quantity'])
            )
            itens.append(item)

        cart.ammount = ammount
        cart.quantity = quantity
        cart.save()

        cart.item.clear()

        for i in itens:
            cart.item.add(i)

        for p in request.data:
            product = ProductService.select_product_not_serialized(request, p['product_id'])
            product.max_availability = product.max_availability - int(p['quantity'])
            product.save()


        return cart
