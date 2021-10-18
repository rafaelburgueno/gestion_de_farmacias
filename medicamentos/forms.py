#encoding:utf-8
from django import forms
from .models import Medicamentos, Presentacion


class MedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamentos
		exclude = ('lote',)

		widgets = {			
			'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
			'presentacion': forms.Select(attrs={'class': 'form-control'}),
			'tipo': forms.Select(attrs={'class': 'form-control'}),
			'fecha_expiracion': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
			
			}

class CrearmedicamentoForm(forms.ModelForm):
	class Meta:
		model = Medicamentos

		widgets = {
				'lote': forms.TextInput(attrs={'class': 'form-control'}),
				'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
				'presentacion': forms.Select(attrs={'class': 'form-control'}),
				'tipo': forms.Select(attrs={'class': 'form-control'}),
				'fecha_expiracion': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
				
			}


class CrearpresentacionForm(forms.ModelForm):
		class Meta:
			model = Presentacion
			widgets = {
				'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			}
