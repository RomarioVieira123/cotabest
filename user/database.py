import re
from random import randrange
from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework import serializers
from validate_docbr import CPF
from user.models import Profile
from django.utils import timezone


class DatabaseUserRepository():

    @classmethod
    @transaction.atomic
    def update_user(cls, request, pk):
        group = request.data.get('group')
        user = cls.select_user(request, pk)
        user.first_name = request.data.get('first_name')
        user.username = request.data.get('username').replace(' ', '_').lower()
        user.email = request.data.get('email')
        user.save()
        user.groups.clear()
        user.profile.group.clear()
        g = cls.select_group(request, group)
        user.profile.group.add(g)
        user.profile.updated_at = timezone.now
        g.user_set.add(user)
        return user

    @classmethod
    @transaction.atomic
    def delete_user(cls, request, pk):
        pass

    @classmethod
    @transaction.atomic
    def insert_user(cls, request, slug=False):
        if slug:
            username = cls.create_slug(request.data.get('first_name'))
        else:
            username = request.data['username']
        user = User.objects.create(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            username=username,
            email=cls.valid_email(request.data.get('email'))
        )
        password = request.data.get('password')
        user.set_password(password)
        user.save()

        return user, password

    @staticmethod
    def valid_email(email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError({"error": "Este email já está cadastrado em nosso sistema"})

        return email

    @classmethod
    def select_user(cls, request, pk):
        user = User.objects.filter(id=pk).first()
        return user

    @classmethod
    def select_all_users(cls):
        users = User.objects.filter().all()
        return users

    @classmethod
    def select_group(cls, request, pk):
        group = Group.objects.get(id=pk)

        return group

    @classmethod
    def create_slug(cls, name):
        list_name = name.split(' ')
        username = ('_'.join([list_name[0], list_name[-1]])).lower()

        if User.objects.filter(username=username):
            username += str(randrange(0, 999))

        return username

    @staticmethod
    def only_numbers(dado):
        return ''.join(re.findall('\d', str(dado)))

    @classmethod
    def valid_cpf(self, number):
        cpf = CPF()
        if cpf.validate(number):
            if Profile.objects.filter(cpf=self.only_numbers(number)):
                raise serializers.ValidationError({"error": "Este CPF já está cadastrado em nosso sistema"})
            return self.only_numbers(number)
        raise serializers.ValidationError({"error": "O CPF é inválido"})

    @classmethod
    @transaction.atomic
    def insert_profile(cls, request, user, group):
        profile = Profile.objects.create(
            user=user,
            cpf=cls.valid_cpf(request.data.get('cpf')),
        )
        profile.group.add(group)
        return profile