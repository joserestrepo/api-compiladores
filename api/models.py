from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Archivos(models.Model):

    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombreArchivo = models.CharField(max_length=100, default='')
    texto = models.TextField( blank=True )
