from django import forms
import datetime

from django.forms import widgets

from gestionStock.models import Farmacias, Lotes


class Formulario_nuevo_stock(forms.ModelForm):

        class Meta:
                model = Lotes
                fields = ['medicamento','stock','ubicacion','vencimiento']

        """
        medicamento = forms.IntegerField()
        stock = forms.IntegerField()
        #ubicacion = forms.ModelChoiceField(Farmacias.objects.all())
        ubicacion = forms.IntegerField()
        #ingreso = forms.DateField(initial=datetime.date.today)
        ingreso = forms.DateField()
        vencimiento = forms.DateField()
        """

class Formulario_nuevo_medicamento(forms.Form):

        nombre_comercial = forms.CharField()
        categoria = forms.CharField()
        laboratorio = forms.CharField()
        principio_activo = forms.CharField()
        forma = forms.CharField()
        contraindicaciones = forms.CharField()


