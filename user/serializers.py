from django.contrib.auth.models import User, Permission, Group
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.facade import RegisterUserFacade
from user.models import Profile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        _user = User.objects.filter(id=user.id).values('id', 'username', 'is_staff', 'is_superuser').first()
        _profile = Profile.objects.filter(user__id=user.id).values('cpf').first()

        token = super().get_token(user)

        token['roles'] = list(user.get_group_permissions())
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['users'] = _user
        token['profile'] = _profile
        token['preferences_user'] = None

        return token


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id',
                  'content_type_id',
                  'codename',
                  'name'
                  ]


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id',
                  'name',
                  'permissions'
                  ]


class ProfileSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['cpf',
                  'group'
                  ]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'username',
            'email',
            'profile',
        ]


class RegisterSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    cpf = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
    is_admin = serializers.BooleanField()

    @transaction.atomic
    def create(self, validated_data):
        user = RegisterUserFacade
        return user.register(validated_data)

    def update(self, instance, validated_data):
        pass