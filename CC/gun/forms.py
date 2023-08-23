from django import forms
from .models import Gun

class PurchaseForm(forms.Form):
    gun = forms.ModelChoiceField(queryset=Gun.objects.all())
    user_id = forms.IntegerField()