from django.contrib.auth.models import Group, Permission, User
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import MyTokenObtainPairSerializer, GroupSerializer, PermissionSerializer, RegisterSerializer, \
    UserSerializer
from user.service import UserService


class MyTokenObtainPairController(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': "User created successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):

    def get(self, request):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('auth.view_user'):
            try:
                users = User.objects.all()
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to add denied"}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    def get(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('auth.view_user'):
            try:
                user = UserService.select_user_serialized(request, pk)
                return Response({'success': True, 'message': None, 'user': user})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to view denied"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('auth.add_user'):
            try:
                user = UserService.insert_user_serialized(request)
                return Response({'success': True, 'message': 'User created successfully', 'user': user})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to add denied"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('auth.change_user'):
            try:
                user = UserService.update_user_serialized(request, pk)
                return Response({'success': True, 'message': 'User updated successfully', 'user': user})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to change denied"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_access = UserService.select_user_not_serialized(request, request.auth.payload['user_id'])
        if user_access.has_perm('auth.delete_user'):
            try:
                UserService.delete_user_not_serialized(request, pk)
                return Response({'success': True, 'message': 'User deleted successfully'})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': "Permission to delete denied"}, status=status.HTTP_400_BAD_REQUEST)


class GroupsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        groups_common = Group.objects.all()
        serializer_common = GroupSerializer(groups_common, many=True)
        return Response({"common": serializer_common.data})


class GroupView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        serializer = GroupSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        form = request.data
        Group.objects.filter(id=pk).update(name=form['group-name'])
        self.save_permissions(request, Group.objects.get(id=pk))

        return Response({'success': 'Grupo atualizado'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        form = request.data
        group = Group.objects.create(name=form['group-name'])
        self.save_permissions(request, group)

        return Response({'success': 'Grupo cadastrado'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_object(pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    @staticmethod
    def save_permissions(request, group):
        permissions = request.data.get('permissions')
        group.permissions.clear()
        for permission in permissions:
            p = Permission.objects.get(id=permission)
            group.permissions.add(p)


class PermissionsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        permissions = Permission.objects.filter(
            content_type_id__in=[4, 7, 8]).all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)
