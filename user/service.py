import json
from django.contrib.auth.models import Group
from django.core import serializers
from django.db import transaction

from user.database import DatabaseUserRepository
from user.serializers import UserSerializer
from user.models import Profile


class UserService():

    @classmethod
    def update_user_serialized(cls, request, pk):
        user = DatabaseUserRepository.update_user(request, pk)
        serializer = UserSerializer(user)

        return serializer.data

    @classmethod
    def update_user_not_serialized(cls, request, pk):
        user = DatabaseUserRepository.update_user(request, pk)
        return user

    @classmethod
    def delete_user_serialized(cls, request, pk):
        pass

    @classmethod
    def delete_user_not_serialized(cls, request, pk):
        user = DatabaseUserRepository.select_user(request, pk)
        user.delete()

    @classmethod
    @transaction.atomic
    def insert_user_serialized(cls, request):
        user, password = DatabaseUserRepository.insert_user(request, True)
        group = cls.set_groups(request, user)
        cls.insert_user_register(request, user, group)
        user_serializer = UserSerializer(user)

        return user_serializer.data

    @classmethod
    def insert_user_not_serialized(cls, request):
        user, password = DatabaseUserRepository.insert_user(request, False)
        cls.set_groups(request, user)
        cls.insert_user_register(request, user)

        return user

    @classmethod
    def select_user_serialized(cls, request, pk):
        user = DatabaseUserRepository.select_user(request, pk)
        user_serializer = UserSerializer(user)

        return user_serializer.data

    @classmethod
    def select_user_not_serialized(cls, request, pk):
        user = DatabaseUserRepository.select_user(request, pk)
        return user

    @classmethod
    def select_all_users_serialized(cls):
        users = DatabaseUserRepository.select_all_users()
        data = serializers.serialize("json", users)
        data_json = json.loads(data)

        return data_json

    @classmethod
    def select_all_users_not_serialized(cls):
        users = DatabaseUserRepository.select_all_users()

        return list(users)

    @classmethod
    def select_group_serialized(cls, request, pk):
        pass

    @classmethod
    def select_group_not_serialized(cls, request, pk):
        group = DatabaseUserRepository.select_group(request, pk)
        return group

    @classmethod
    def set_groups(cls, request, user):
        group = cls.select_group_not_serialized(request, request.data['group'])
        group.user_set.add(user)
        return group

    @classmethod
    def set_user_admin(cls, user):
        group, _ = Group.objects.get_or_create(name='admin')
        group.user_set.add(user)

    @classmethod
    def insert_user_register(cls, request, user, group):
        DatabaseUserRepository.insert_profile(request, user, group)