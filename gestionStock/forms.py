from django import forms
import datetime

from django.forms import widgets

from gestionStock.models import Medicamentos


class Formulario_nuevo_medicamento(forms.Form):

        class Meta:
                model = Medicamentos
                fields = ['nombre_comercial','categoria','laboratorio','principio_activo','forma','contraindicaciones']

        """
        nombre_comercial = forms.CharField()
        categoria = forms.CharField()
        laboratorio = forms.CharField()
        principio_activo = forms.CharField()
        forma = forms.CharField()
        contraindicaciones = forms.CharField()
        """

