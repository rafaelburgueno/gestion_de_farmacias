from django import forms
from django.forms import widgets

from gestionUsuarios.models import Usuarios


class FormularioUsuario(forms.ModelForm):
        #formulario de registro de un Usuario en la base de datos

       

        #password1 es la contraseña
        #password2 es la verificacion de la contraseña

        password1 = forms.CharField(label='Contraseñases', widget=forms.PasswordInput(
                attrs={
                        'class':'form-control',
                        'placeholder': 'Ingrese su contraseña...',
                        'id':'password1',
                        'required':'required'
                }
        ))
        
        password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
                attrs={
                        'class':'form-control',
                        'placeholder': 'Ingrese nuevamente su contraseña...',
                        'id':'password2',
                        'required':'required',
                }
        ))

        #rol.widget.attrs.update({'class': 'btn btn-danger'})

        class Meta:
                model= Usuarios
                fields = ['cedula_de_identidad','rol','usuario','email','nombre','apellido']
                
                #widgets = {'apellido': forms.TextInput(attrs={'class': 'btn'}),}

                """
                widgets = {'cedula_de_identidad': forms.IntegerField(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Ingrese su cedula de identidad...',
                                }
                        ),
                        'usuario': forms.TextInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Ingrese un usuario...',
                                }
                        ),
                        'email': forms.EmailInput(
                                attrs={
                                        'class':'form-control',
                                        'placeholder':'Correo Electrónico...',
                                }
                        ),
                        
                }"""


        def clean_password2(self):
                #validacion de contraseñas

                password1 = self.cleaned_data.get("password1")
                password2 = self.cleaned_data.get("password2")
                if password1 and password2 and password1 != password2:
                        raise forms.ValidationError("Las contraseñas no coinciden.")
                return password2

        def save(self, commit = True):
                user = super().save(commit = False)
                user.set_password(self.cleaned_data.get('password1'))
                if commit:
                        user.save()
                return user



