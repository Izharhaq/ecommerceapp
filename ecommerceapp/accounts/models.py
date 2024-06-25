from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_subuser = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

