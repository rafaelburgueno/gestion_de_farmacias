from django import forms
import datetime


class Formulario_lotes(forms.Form):

        medicamento = forms.CharField()
        stock = forms.IntegerField()
        #ubicacion (id_farmacia)
        ingreso = forms.DateField(initial=datetime.date.today)
        vencimiento = forms.DateField(initial=datetime.date.today)


class Formulario_nuevo_medicamento(forms.Form):

        nombre_comercial = forms.CharField()
        categoria = forms.CharField()
        laboratorio = forms.CharField()
        principio_activo = forms.CharField()
        forma = forms.CharField()
        contraindicaciones = forms.CharField()
