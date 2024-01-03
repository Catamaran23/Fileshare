from django.contrib import admin

from Formulaire.models import Personne, Fichier

@admin.register(Personne,Fichier)
class Generic_admin(admin.ModelAdmin):
    pass
# Register your models here.
