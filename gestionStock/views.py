from django.shortcuts import render, redirect

# vistas basadas en clases
from django.views.generic import TemplateView, ListView, CreateView, View, UpdateView

# Importacion de los Modelos
from gestionStock.models import Medicamentos

# FORMULARIOS
from gestionStock.forms import Formulario_nuevo_medicamento

#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy



# =======================================================================
# Medicamentos ==========================================================
# =====================================================================
class ListarMedicamentos(ListView):
        model = Medicamentos
        form_class = Formulario_nuevo_medicamento
        context_object_name = "medicamentos"
        template_name = 'medicamentos.html'
        paginate_by = 100  # if pagination is desired
    #busqueda_por_farmacias = Lotes.objects.filter(ubicacion="miFarmacia")
    #busqueda_por_farmacias = Lotes.objects.filter(ubicacion__icontains="miFarmacia")


        
    
        
