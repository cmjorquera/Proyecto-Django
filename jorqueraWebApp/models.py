from django.db import models

# Create your models here.



class Personas (models.Model):
    nombre           = models.CharField(max_length=30, verbose_name= "El Nombre") 
    edad             = models.CharField(max_length=30, verbose_name= "La Edad") 
    apellido_mater   = models.CharField(max_length=30, verbose_name= "El Apellido materno") 
    apellido_pater   = models.CharField(max_length=30, verbose_name= "El Apellido Paterno") 
    direccion        = models.CharField(max_length=50,verbose_name= "La Direccion")     #verbose_name= 'La Direccion'
    email            = models.EmailField(blank= True, null= True, verbose_name = "El mail") # NO OBLIGATORIO
    telefono         = models.CharField(max_length=13, verbose_name = "El Telefono")
    comentario       = models.CharField(max_length=30, verbose_name= "El Comentario") 
    
