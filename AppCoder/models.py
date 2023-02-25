from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    curso = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Comentario(models.Model):
    comentario = models.CharField(max_length=1200)
    firma = models.CharField(max_length=50)
    def __str__(self):
	    return f"{self.comentario}"

class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"