from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=20, default='', blank=True)
    group = models.ManyToManyField(Group, related_name='group')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)