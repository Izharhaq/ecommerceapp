from django.contrib import admin

# Register your models here.

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'is_subuser']

admin.site.register(CustomUser, CustomUserAdmin)
