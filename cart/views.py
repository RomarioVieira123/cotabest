from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer
from user.service import UserService
from cart.service import CartService


class CartsView(APIView):

    def get(self, request):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.view_product'):
            try:
                cart = Cart.objects.all()
                serializer = CartSerializer(cart, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)


class CartView(APIView):

    def get(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.view_product'):
            try:
                cart = CartService.select_cart_serialized(request, pk)
                return Response({'success': True, 'message': None, 'cart': cart})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.add_product'):
            try:
                cart = CartService.insert_cart_serialized(request)
                return Response({'success': True, 'message': 'Cart created successfully', 'cart': cart})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to add denied"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.change_product'):
            try:
                cart = CartService.update_cart_serialized(request, pk)
                return Response({'success': True, 'message': 'Cart updated successfully', 'cart': cart})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to change denied"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.delete_product'):
            try:
                CartService.delete_cart_serialized(request, pk)
                return Response({'success': True, 'message': 'Cart deleted successfully'})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to delete denied"}, status=status.HTTP_400_BAD_REQUEST)
