from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    name = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["username", "password", "email", "name"]
