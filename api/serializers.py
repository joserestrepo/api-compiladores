from rest_framework import serializers
from .models import Archivos

class ArchivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Archivos
        fields = ('id', 'id_user', 'nombreArchivo', 'texto')
