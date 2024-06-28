# from rest_framework.permissions import BasePermission

# class IsAdminOrHasEditPermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_admin:
#             return True
#         if request.user.is_subuser:
#             # Add logic to check if the user has edit permission for the specific object
#             return obj.owner == request.user
#         return False

#************************************************************************
'''
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
    ])

********* permission model *********
class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

******************
class CustomUser(AbstractUser):
    # ...
    permissions = models.ManyToManyField(Permission, related_name='users')

***************
def assign_permissions(user):
    if user.role == 'admin':
        permissions = Permission.objects.filter(name__in=['can_create_user', 'can_edit_user', 'can_delete_user'])
    elif user.role == 'moderator':
        permissions = Permission.objects.filter(name__in=['can_edit_user', 'can_delete_user'])
    else:
        permissions = Permission.objects.filter(name__in=['can_view_user'])
    user.permissions.set(permissions)

****************
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def create_user_view(request):
    if not request.user.has_perm('can_create_user'):
        return HttpResponseForbidden()
    # ...
    return render(request, 'create_user.html')

****************
# {% if request.user.has_perm 'can_edit_user' %}
#     <a href="{% url 'edit_user' user.id %}">Edit User</a>
# {% endif %}
**************************
from django.contrib.auth.signals import user_saved

def assign_permissions_on_save(sender, instance, created, **kwargs):
    assign_permissions(instance)

user_saved.connect(assign_permissions_on_save)

'''