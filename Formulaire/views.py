from django.http import HttpResponse 
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from Formulaire.models import Personne,Fichier
from Formulaire.serializers import PersonneSerializer,FichierSerializer
# Create your views here.

class PersonneViewset(viewsets.ModelViewSet):
    queryset= Personne.objects.all()
    serializer_class=PersonneSerializer
    permission_classes=(IsAuthenticated, )
    filterset_fields=['first_name','last_name']
    search_fields=['last_name']
class FichierViewset(viewsets.ModelViewSet):
    queryset= Fichier.objects.all()
    serializer_class=FichierSerializer
    permission_classes=(IsAuthenticated, )
    filterset_fields=['date_upload']