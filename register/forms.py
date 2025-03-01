from django import forms
from .models import CustomUser

class CreateNewUser(forms.Form):
    model = CustomUser
    username = forms.CharField(max_length=200)
    fields = ['username']
