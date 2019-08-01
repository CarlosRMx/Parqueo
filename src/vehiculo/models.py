from django.db import models
# Create your models here.
class Vehiculo(models.Model):
    matricula=models.CharField(max_length=10)
    color=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)

    def __str__(self):
        return self.matricula+" "+self.marca+" "+self.color


