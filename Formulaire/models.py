from django.db import models
class Personne(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #list = models.ForeignKey('Fichier',null=False, on_delete=models.CASCADE)
class Fichier(models.Model):
    fichier = models.FileField(upload_to='fichiers/')
    date_upload = models.DateTimeField(auto_now_add=True)
  

# Create your models here.
