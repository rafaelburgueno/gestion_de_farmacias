from django.db import models
from django.db.models.base import Model
import datetime

#==============
# Medicamentos =
#==============
class Medicamentos(models.Model):

        nombre_comercial = models.CharField(max_length=100)
        categoria = models.CharField(max_length=50, verbose_name='Categoria(venta libre, receta verde o FNR)')
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
        direccion = models.CharField(max_length=100, blank=True, null=True)
        localidad = models.CharField(max_length=100)
        departamento = models.CharField(max_length=50, blank=True, null=True)

        def __str__(self):
                return self.nombre + " " + self.localidad + " " + self.departamento
        



#=======
# Lotes =
#=======
class Lotes(models.Model):
        #medicamento (id_medicamento)
        medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
        stock = models.IntegerField()
        #ubicacion (id_farmacia)
        ubicacion = models.ForeignKey(Farmacias, on_delete=models.CASCADE)
        ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de ingreso",blank=True, null=True)
        vencimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de vencimiento")

        #created = models.CharField(verbose_name="Fecha de creación", max_length=100, blank=True, default=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True, null=True)
        updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True, null=True)

        def __str__(self):
                return str(self.stock) + " unidades de " + str(self.medicamento) + " con vencimiento " + str(self.vencimiento)
        



