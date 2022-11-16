from cart.models import Cart


class DatabaseCartRepository:

    @classmethod
    def select_cart(cls, request, pk):
        cart = Cart.objects.filter(user__id=pk).first()
        return cart

    @classmethod
    def select_all_carts(cls):
        carts= Cart.objects.filter().all()
        return carts
