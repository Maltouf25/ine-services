from django import forms
from .models import Suivi

class suiviform(forms.Form):
    id=forms.IntegerField(widget=forms.TextInput(attrs={
        'id':'title',
        'placeholder':"Entrer l'ID de votre réclamation..."                
        }))