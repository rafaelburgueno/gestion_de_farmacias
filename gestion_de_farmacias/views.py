from django.db.models.query import QuerySet
from django.http import HttpResponse

# vistas basadas en clases
from django.views.generic import TemplateView, ListView, CreateView, View, UpdateView

#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

# from django.template import Template, Context
import datetime
# import os
# import json
# from django.template.loader import get_template
from django.shortcuts import render, redirect

from gestion_de_farmacias import settings

# importaciones necesarias para enviar emails
from django.conf import settings
from django.core.mail import send_mail

# Importacion de los Modelos
from gestionStock.models import Lotes, Medicamentos

# FORMULARIOS
from gestion_de_farmacias.forms import Formulario_nuevo_stock, Formulario_nuevo_medicamento


# ===============================================================
# funciones que dan respuesta a las peticion provenientes de urls.py  =
# ===============================================================


# ========
# Inicio =
# ========
def inicio(request):

    lista_personas = [{
        'picture': 'http://placehold.it/32x32',
        'age': 40,
        'name': 'Velez William',
        'email': 'velezwilliam@pearlesex.com'
    },
        {
        'picture': 'http://placehold.it/32x32',
        'age': 37,
        'name': 'Walsh Gibbs',
        'email': 'walshgibbs@pearlesex.com'
    },
    ]

    # json_personas= json.dumps(lista_personas)
    # json_personas= json.dumps([11,12,13,14,15])
    json_personas = [11, 12, 13, 14, 15]

    diccionario_de_contexto = {
        "datos_json": json_personas, "usuario": "Rafael Burgueño"}

    return render(request, "inicio.html", diccionario_de_contexto)




# ====================
# Buscar Medicamento =
# ==================
def buscar_medicamento(request):

    mensaje = ""
    diccionario_de_contexto = {
        "usuario": "Rafael Burgueño", "mensaje": mensaje}

    if request.GET["termino_buscado"]:

        termino_buscado = request.GET["termino_buscado"]

        if len(termino_buscado) > 20:
            mensaje = "El termino buscado es demasiado extenso."
            diccionario_de_contexto = {
                "usuario": "Rafael Burgueño", "mensaje": mensaje}
        else:
            # __icontains busca la palabra en elguna parte del registro
            medicamentos = Medicamentos.objects.filter(
                nombre_comercial__icontains=termino_buscado)
            # mensaje = "Se encontraron %r medicamentos" % len(medicamentos)
            diccionario_de_contexto = {"medicamentos": medicamentos,
                                       "termino_buscado": termino_buscado, "usuario": "Rafael Burgueño", "mensaje": mensaje}

    return render(request, "medicamentos.html", diccionario_de_contexto)




# =======================================================================
# Stock =================================================================
# =====================================================================
class Stock(View):
    model = Lotes
    form_class = Formulario_nuevo_stock
    template_name = 'stock.html'
    #busqueda_por_farmacias = Lotes.objects.filter(ubicacion="miFarmacia")
    #busqueda_por_farmacias = Lotes.objects.filter(ubicacion__icontains="miFarmacia")

    # este metodo devuelve la consulta principal de la vista
    def get_queryset(self):
        return Lotes.objects.all()
    
    # este metodo devuelve el diccionario de contexto(los datos) que va a ser enviado al template
    def get_context_data(self, **kwargs):
        diccionario_de_contexto = {}
        diccionario_de_contexto["lotes_list"] = self.get_queryset()

        #formulario_nuevo_stock
        diccionario_de_contexto["formulario_nuevo_stock"] = self.form_class
        return diccionario_de_contexto
    
    # este metodo devuelve toda la informacion cuando se hagan este tipo de peticiones
    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    

    def post(self,request, *args, **kwargs):
        formulario_nuevo_stock = self.form_class(request.POST)

        if formulario_nuevo_stock.is_valid():
            formulario_nuevo_stock.save()
            return redirect('stock')
        


# =======================================================================
# Editar Stock ===========================================================
# =======================================================================
class EditarStock(UpdateView):
    model = Lotes
    form_class = Formulario_nuevo_stock
    template_name = 'editar_stock.html'

    success_url = reverse_lazy('stock')





# =======
# Login =
# =======
class LoginPageView(TemplateView):

    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        diccionario_de_contexto = {"usuario": "Rafa"}
        return render(request, self.template_name, diccionario_de_contexto)


"""def login(request):

	diccionario_de_contexto={"usuario":"Rafael Burgueño"}

	return render(request, "login.html", diccionario_de_contexto)

"""


# =========
# Recetas =
# =========
# def receta(request, receta_numero,usuario):
def recetas(request):

    mensaje = ""

    if request.method == "POST":

        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " --- " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["rafaelburg@gmail.com"]

        send_mail(subject, message, email_from, recipient_list)

        mensaje = "Gracias. Se enviaron datos por POST"

    recetas = ["receta 1", "receta 2", "receta 3", "receta 4"]

    diccionario_de_contexto = {
        "usuario": "Rafael Burgueño", "recetas": recetas, "mensaje": mensaje}

    return render(request, "recetas.html", diccionario_de_contexto)


# =========
# Usuario =
# =========
def usuario(request):

    diccionario_de_contexto = {"usuario": "Rafael Burgueño"}

    return render(request, "usuario.html", diccionario_de_contexto)


# =============================
# Funcion para hacer busquedas =
# =============================
def buscar(termino_buscado, modelo):

    mensaje = ''

    if len(termino_buscado) > 20:
        mensaje = "El termino buscado es demasiado extenso."
        diccionario_de_contexto = {
            "usuario": "Rafael Burgueño", "mensaje": mensaje}
    else:
        # __icontains busca la palabra en elguna parte del registro
        medicamentos = modelo.objects.filter(
            nombre_comercial__icontains=termino_buscado)
        # mensaje = "Se encontraron %r medicamentos" % len(medicamentos)
        diccionario_de_contexto = {"medicamentos": medicamentos,
                                   "termino_buscado": termino_buscado, "usuario": "Rafael Burgueño", "mensaje": mensaje}

    return
