from django.db import models
from propietario.models import Propietario
# Create your models here.
class Ticket(models.Model):
    hora_ingreso=models.DateTimeField()
    hora_salida=models.DateTimeField()
    propietario=models.ForeignKey(Propietario,on_delete=models.CASCADE)
    costo=models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.BooleanField(default=0)

   # def __str__(self):
    #    return self.costo

    
