from django import forms
from gestionUsuarios.models import ModelForm, Usuario
class usuarios(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
