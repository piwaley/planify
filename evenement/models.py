from django.db import models

# Create your models here.


class Evenement(models.Model):
    nom = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField()
    date_event = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    duree = models.CharField(max_length=256, null=False, blank=False)
    lieu = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    adresse = models.TextField()
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True, auto_now_add=True)
