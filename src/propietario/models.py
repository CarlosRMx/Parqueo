from django.db import models
from vehiculo.models import Vehiculo
# Create your models here.
class Propietario(models.Model):
    nombre_propietario=models.CharField(max_length=30)
    apellido_propietario=models.CharField(max_length=30)
    no_dpi=models.CharField(max_length=20)
    vehiculo=models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_propietario + " " +self.apellido_propietario 

   