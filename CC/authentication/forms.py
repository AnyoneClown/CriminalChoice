from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    role = forms.ChoiceField(choices=((1, 'Mafia'), (2, 'Gang')))
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

class BetForm(forms.Form):
    amount = forms.IntegerField()
    