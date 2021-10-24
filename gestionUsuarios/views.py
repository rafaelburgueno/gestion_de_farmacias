from django.shortcuts import render
from django.urls import reverse_lazy

# vistas basadas en clases
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView

from gestionUsuarios.models import Usuarios

from gestionUsuarios.forms import FormularioUsuario

class Usuario(TemplateView):
        model = Usuarios

        template_name = 'usuario.html'


class ListaDeUsuarios(ListView):
        model = Usuarios

        template_name = 'lista_de_usuarios.html'
        
        def get_queryset(self) :
                #return self.objects.filter(usuario_activo=True)
                #print(self.model.objects.filter(usuario_activo=True))
                return self.model.objects.filter(usuario_activo=True)

class RegistrarUsuario(CreateView):
        model = Usuarios
        form_class = FormularioUsuario

        template_name = 'registrar_usuario.html'
        success_url = reverse_lazy('lista_de_usuarios')





class EditarUsuario(UpdateView):
        model = Usuarios
        form_class = FormularioUsuario

        template_name = 'editar_usuario.html'
        success_url = reverse_lazy('usuario')


#
