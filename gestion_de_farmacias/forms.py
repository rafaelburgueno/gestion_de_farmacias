from django import forms
import datetime

from gestionStock.models import Farmacias


class Formulario_nuevo_lote(forms.Form):

        medicamento = forms.IntegerField()
        stock = forms.IntegerField()
        #ubicacion = forms.ModelChoiceField(Farmacias.objects.all())
        ubicacion = forms.IntegerField()
        #ingreso = forms.DateField(initial=datetime.date.today)
        ingreso = forms.DateField()
        vencimiento = forms.DateField()


class Formulario_nuevo_medicamento(forms.Form):

        nombre_comercial = forms.CharField()
        categoria = forms.CharField()
        laboratorio = forms.CharField()
        principio_activo = forms.CharField()
        forma = forms.CharField()
        contraindicaciones = forms.CharField()
