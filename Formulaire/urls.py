from django.urls import path
from rest_framework import routers
from Formulaire.views import PersonneViewset,FichierViewset
from . import views
from django.urls import path,include
 
router =routers.DefaultRouter()
router.register('Personne',PersonneViewset)
router.register('Fichier',FichierViewset)

urlpatterns = [
   # path("", views.index),
    path('Formulaire/',include ("Formulaire.urls")),
]