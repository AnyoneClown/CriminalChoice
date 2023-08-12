from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    role = forms.ChoiceField(choices=((1, 'mafia'), (2, 'gang')))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']