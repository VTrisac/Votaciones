from django.db import models

# Create your models here.

class Voto(models.Model):
    partido = models.TextField()
    color = models.TextField()
    votos = models.IntegerField()
