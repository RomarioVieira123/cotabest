import re
from random import randrange

from django.contrib.auth.models import User, Group
from django.db import transaction
from rest_framework import serializers
from validate_docbr import CPF

from user.models import Profile


class CreateUser:

    def create(self, data, slug=False):
        if slug:
            username = self.create_slug(data.get('first_name'))
        else:
            username = data['username']
        user = User.objects.create(
            first_name=data.get('first_name'),
            username=username,
            email=self.valid_email(data.get('email'))
        )
        password = data['password']
        user.set_password(password)
        user.save()

        return user, password

    @staticmethod
    def create_slug(name):
        list_name = name.split(' ')
        username = ('_'.join([list_name[0], list_name[-1]])).lower()
        if User.objects.filter(username=username):
            username += str(randrange(0, 999))

        return username

    @staticmethod
    def set_user_admin(user):
        group, _ = Group.objects.get_or_create(name='Administradores')
        group.user_set.add(user)

        return group

    @staticmethod
    def set_user_default(user):
        group, _ = Group.objects.get_or_create(name='Comuns')
        group.user_set.add(user)

        return group


    @staticmethod
    def set_group(data, user):
        g = Group.objects.get(id=data['group'])
        g.user_set.add(user)

    @staticmethod
    def valid_email(email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError({"error": "Este email já está cadastrado em nosso sistema"})

        return email


class CreateProfile:

    def create(self, data, user, group):
        profile = Profile.objects.create(
            user=user,
            cpf=self.valid_cpf(data.get('cpf')),
        )
        profile.group.add(group)

    @staticmethod
    def only_numbers(dado):
        return ''.join(re.findall('\d', str(dado)))

    def valid_cpf(self, number):
        cpf = CPF()
        if cpf.validate(number):
            if Profile.objects.filter(cpf=self.only_numbers(number)):
                raise serializers.ValidationError({"error": "Este CPF já está cadastrado em nosso sistema"})
            return self.only_numbers(number)
        raise serializers.ValidationError({"error": "O CPF é inválido"})


class CreateUserFacade:

    @transaction.atomic
    def create(self, data):
        create_user = CreateUser()
        user, password = create_user.create(data, slug=True)
        create_user.set_group(data, user)
        profile = CreateProfile()
        profile.create(data, user)


class RegisterUserFacade:

    @staticmethod
    def register(data):
        create_user = CreateUser()
        user, password = create_user.create(data, slug=True)
        if data['is_admin']:
            group = create_user.set_user_admin(user)
        else:
            group = create_user.set_user_default(user)
        profile = CreateProfile()
        profile.create(data, user, group)

        return user