from django.db import models

# Create your models here.
class Dios(models.Model):
    dios = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion= models.DateField(null=True)
    
    def __str__(self):
        return f'Hola, soy el dios: {self.dios}'
     