from rest_framework import serializers
from Formulaire.models import Personne, Fichier

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personne 
        fields='__all__'
class FichierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fichier
        fields='__all__'