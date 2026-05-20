from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Game info", {"fields": ("kingdom",)}),)

    add_fieldsets = UserAdmin.add_fieldsets + (("Game info", {"fields": ("kingdom",)}),)

    list_display = ("username", "email", "kingdom", "is_staff", "is_active")
    list_filter = ("kingdom", "is_staff", "is_active")
