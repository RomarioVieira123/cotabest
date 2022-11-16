from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=20, default='', blank=True)
    group = models.ManyToManyField(Group, related_name='group')