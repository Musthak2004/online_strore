from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "phone_number")

    def clean_email(self):
        return self.cleaned_data["email"].lower()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "phone_number", "is_vendor", "is_active", "is_staff")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "address",
            "district",
            "city",
            "postal_code",
            "profile_picture"
        ]

        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }

        labels = {
            "postal_code": "Postal Code",
            "profile_picture": "Profile Photo"
        }
