from django.db import models
from django.db.models.base import Model

#==============
# Medicamentos =
#==============
class Medicamentos(models.Model):

        nombre_comercial = models.CharField(max_length=100)
        categoria = models.CharField(max_length=50)
        laboratorio = models.CharField(max_length=100)
        principio_activo = models.CharField(max_length=200)
        forma = models.CharField(max_length=50, blank=True, null=True)
        contraindicaciones = models.CharField(max_length=1000)

        def __str__(self):
                return self.nombre_comercial
        



#===========
# Farmacias =
#===========
class Farmacias(models.Model):
        nombre = models.CharField(max_length=100)
        localidad = models.CharField(max_length=100)
        departamento = models.CharField(max_length=50, blank=True, null=True)

        def __str__(self):
                return self.nombre + " " + self.localidad + " " + self.departamento
        



#=======
# Lotes =
#=======
class Lotes(models.Model):
        #medicamento (id_medicamento)
        stock = models.IntegerField()
        #ubicacion (id_farmacia)
        vencimiento = models.DateField()

        def __str__(self):
                return self.stock + " unidades de " + "self.medicamento" + " con vencimiento " + self.vencimiento
        



