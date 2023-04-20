from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
lieux = (
    ("pav1", "Pavillon 1"),
    ("pav2", "Pavillon 2"),
    ("pav3", "Pavillon 3"),
    ("Ascensseur", "Ascensseur"),
    ("autre", "Autre"),
)
class Reclamation(models.Model):
    Nom_complet=models.CharField(max_length=20,null=True)
    Numéro_de_Téléphone=models.IntegerField(null=True)
    Lieu_concerné=models.CharField(max_length=10,choices=lieux,default='nizar') 
    Numéro_de_chambre=models.IntegerField(blank=True,null=True)
    Description=models.TextField()
    Pièce_jointe=models.FileField(blank=True,null=True)
    time=models.DateTimeField()
    traitement=models.BooleanField(default=False)
    terminer=models.BooleanField(default=False)
    reparer=models.BooleanField(default=False)

class Suivi(models.Model):
    object_id=models.IntegerField(primary_key=True)