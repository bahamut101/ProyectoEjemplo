from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField (max_length=30)
    direccion = models.CharField (max_length=40)
    tfno = models.CharField (max_length=9, verbose_name="teléfono")
    email = models.EmailField (blank=True, null=True) # Esto permite valor y campo vacio

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    nombre = models.CharField (max_length=20)
    rama = models.CharField (max_length=20)
    precio = models.FloatField () 

    def __str__(self): # Convertimos a String la salida mediante una función 
        return 'Curso de %s, de la rama %s - PVP: %s€' %(self.nombre,self.rama,self.precio)

class Pedidos(models.Model):
    ref = models.IntegerField()
    fecha = models.DateField()
    finalizado = models.BooleanField() #finalizado o no