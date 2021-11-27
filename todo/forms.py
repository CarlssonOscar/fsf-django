from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Ovanstående gör användning funktioner från forms.ModelForm möjlig
    class Meta:
        model = Item
        fields = ['name', 'done']
