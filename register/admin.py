from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserManager(UserAdmin):
    list_display = ['username', 'email', 'followers', 'following']
    search_fields = ['username']