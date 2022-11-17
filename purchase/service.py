import json
from cart.serializers import CartSerializer
from cart.service import CartService
from purchase.database import DatabasePurchaseRepository
from purchase.serializers import PurchaseSerializer
from django.core import serializers


class PurchaseService:

    @classmethod
    def select_purchase_by_not_user_serialized(cls, request, pk):
        purchase = DatabasePurchaseRepository.select_purchase_by_user(request, pk)

        return purchase

    @classmethod
    def select_purchase_by_user_serialized(cls, request, pk):
        purchase = DatabasePurchaseRepository.select_purchase_by_user(request, pk)
        purchase_serializer = PurchaseSerializer(purchase)

        return purchase_serializer.data

    @classmethod
    def create_purchase(cls, request, pk):
        purchase_serializer = None
        cart = CartService.select_cart_not_serialized_by_user(request, pk)
        purchase = cls.select_purchase_by_not_user_serialized(request, pk)
        if purchase is not None:
            raise Exception("User already has an open purchase.")
        elif cart is None:
            raise Exception("There is no open affection for this user")
        else:
            cart_serialized = CartService.select_cart_serialized_by_user(request, pk)
            p = DatabasePurchaseRepository.save(request, cart_serialized)
            purchase_serializer = PurchaseSerializer(p)

        return purchase_serializer.data

    @classmethod
    def delete_purchase(cls, request, pk):
        purchase = cls.select_purchase_by_user_serialized(request,pk)
        purchase_serializer = PurchaseSerializer(purchase)
        DatabasePurchaseRepository.delete_purchase(purchase_serializer)

        return None

    @classmethod
    def select_all_users_serialized(cls, pk):
        purchases = DatabasePurchaseRepository.select_all_purchases(pk)
        data = serializers.serialize("json", purchases)
        data_json = json.loads(data)

        return data_json
