from django.db import transaction

from cart.service import CartService
from product.service import ProductService
from purchase.models import Purchase, PurchaseItem


class DatabasePurchaseRepository:

    @classmethod
    def select_purchase_by_user(cls, request, pk):
        purchase = Purchase.objects.filter(user__id=pk).first()
        return purchase

    @classmethod
    def select_purchase(cls, pk):
        purchase = Purchase.objects.filter(id=pk).first()
        return purchase



    @classmethod
    def select_all_purchases(cls, pk):
        purchases = Purchase.objects.filter(user__id=pk).all()
        return purchases

    @classmethod
    @transaction.atomic
    def save(cls, request, cart_serializer):

        purchase = Purchase.objects.create(
            user=request.user,
            total_price=cart_serializer['ammount']
        )

        for i in cart_serializer['item']:
            product = ProductService.select_product_not_serialized(request, i['product']['id'])

            item = PurchaseItem.objects.create(
                product=product,
                quantity=int(i['quantity'])
            )

            purchase.item.add(item)

        CartService.delete_cart_not_serialized(request, request.user.id)

        return purchase
