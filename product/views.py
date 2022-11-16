from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer
from user.service import UserService
from product.service import ProductService


class ProductsView(APIView):

    def get(self, request):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.view_product'):
            try:
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):

    def get(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.view_product'):
            try:
                product = ProductService.select_product_serialized(request, pk)
                return Response({'success': True, 'message': None, 'product': product})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)


class ProductSearchView(APIView):

    def get(self, request):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('product.view_product'):
            try:
                products = ProductService.search_products_not_serialized(request)
                return Response({'success': True, 'message': None, 'products': products})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)
