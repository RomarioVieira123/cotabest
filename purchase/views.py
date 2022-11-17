from rest_framework.views import APIView
from purchase.service import PurchaseService
from user.service import UserService
from rest_framework.response import Response
from rest_framework import status


class PurchaseView(APIView):

    def get(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('purchase.view_purchase'):
            try:
                purchase = PurchaseService.select_purchase_by_user_serialized(request, pk)
                return Response({'success': True, 'message': None, 'purchase': purchase})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('purchase.add_purchase'):
            try:
                purchase = PurchaseService.create_purchase(request, pk)
                return Response({'success': True, 'message': None, 'purchase': purchase})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to create denied"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('purchase.add_purchase'):
            try:
                purchase = PurchaseService.create_purchase(request, pk)
                return Response({'success': True, 'message': None, 'purchase': purchase})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to create denied"}, status=status.HTTP_400_BAD_REQUEST)
