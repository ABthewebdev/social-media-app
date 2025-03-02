from django import forms
from .models import CustomUser
from django.contrib.auth import login, authenticate

class CreateNewUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']