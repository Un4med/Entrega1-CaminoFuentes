from django.db import models

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=250)
    sub_titulo = models.CharField(max_length=250)
    contenido = models.CharField(max_length=500)
    autor = models.CharField(max_length=500)
    fecha_creacion= models.DateField(null=True)
    
    def __str__(self):
        return f'{self.titulo} {self.titulo} {self. contenido}'
     
