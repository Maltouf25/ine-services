from django import forms
from .models import Reclamation

lieux = (
    ("pav1", "Pavillon 1"),
    ("pav2", "Pavillon 2"),
    ("pav3", "Pavillon 3"),
    ("Ascensseur", "Ascensseur"),
    ("autre", "Autre"),)

class Reclamationform(forms.Form):
    Nom_complet=forms.CharField(max_length=20,label='Nom_complet',widget=forms.TextInput(attrs={
        'id':'title',
        'placeholder':"Entrer votre nom..."                
        }))
    Numéro_de_Téléphone=forms.IntegerField(widget=forms.NumberInput(attrs={
        'id':'title',
        'placeholder':"Entrer votre Numéro de téléphone..."             
        }))
    Lieu_concerné=forms.ChoiceField(choices=lieux,required=True) 
    Numéro_de_chambre=forms.IntegerField(required=False,widget=forms.NumberInput(attrs={
        'id':'title',
        'placeholder':"Entrer le numéro de chambre..."
        
        }))
    Description=forms.CharField(max_length=500,widget=forms.Textarea(attrs={
        'id':'title',
        'placeholder':"Entrer la description précise de votre réclamation..."
        
        }))
    Pièce_jointe=forms.FileField(required=False)