from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileForm
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("email", "username", "phone_number", "is_vendor", "is_staff", "is_active")
    list_filter = ("is_vendor", "is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal Info", {"fields": ("phone_number",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "is_vendor", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "phone_number", "password1", "password2", "is_staff", "is_active"),
        }),
    )

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "district", "postal_code")
    search_fields = ("user__email", "city", "district")
    list_filter = ("district", "city")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)