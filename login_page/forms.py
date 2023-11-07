from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ItemModel
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ItemModelForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ['title', 'image', 'description', 'price', 'product_type']

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
