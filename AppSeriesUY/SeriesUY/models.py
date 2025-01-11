from django.db import models

class Usuario(models.Model):
    rol = models.CharField(max_length=30)
    nombreUsuario = models.CharField(max_length=30)
    correo = models.EmailField()
    
    def __str__(self):
        return f'Usuario: {self.nombreUsuario} Correo: {self.correo}'

class Serie(models.Model):
    titulo = models.CharField(max_length=30)
    puntuacion = models.FloatField()
    
    def __str__(self):
        return f'Titulo: {self.titulo} Puntuacion: {self.puntuacion}'
    
class Plataforma(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    
    def __str__(self):
        return f'Plataforma: {self.nombre} Precio: {self.precio}'