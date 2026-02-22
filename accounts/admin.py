from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ["email", "username", "phone_number", "is_staff", "is_active"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('email', 'phone_number', 'is_vendor',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'phone_number', 'is_vendor',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
