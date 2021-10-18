from django.db import models
from django.db.models import signals

import decimal
import datetime
# Create your models here.
TAX_VALUE = 0.18

# Create your models here.
class Presentacion(models.Model):
	
	nombre = models.CharField(max_length=60)

	def __unicode__(self):
		return u'%s' % (self.nombre)

class Medicamentos(models.Model):
	TIPO = (
        ('generico', 'Generico'),
        ('comercial', 'Comercial'),
    )
	lote = models.CharField(max_length=10, unique=True, default=0)
	presentacion = models.ForeignKey(Presentacion,on_delete=models.CASCADE, help_text='Presentacion', verbose_name='Presentacion')	
	tipo = models.CharField(choices=TIPO, max_length=30)
	nombre = models.CharField(max_length=200, unique=True)
	componente = models.CharField(max_length=200)
	concentracion = models.CharField(max_length=50)
	fecha_expiracion = models.DateField()
	descripcion = models.TextField(max_length=400)		
	stock = models.PositiveSmallIntegerField()
	

	def __unicode__(self):
		return self.nombre

	

	def estadomedicamentos(self):
		hoy = datetime.date.today()
		dias = (self.fecha_expiracion - hoy).days
		return dias

	def incrementarlote(self, *args, **kwargs):
		if self.lote == 0:
			self.lote += 1
			self.store.save()
		super(Medicamentos, self).save(*args, **kwargs)



	