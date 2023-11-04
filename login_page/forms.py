# appname/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    # You can add additional fields here if needed

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Adjust as needed
