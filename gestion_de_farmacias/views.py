from django.http import HttpResponse

# vistas basadas en clases
from django.views.generic import TemplateView, ListView, CreateView

#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

# from django.template import Template, Context
import datetime
# import os
# import json
# from django.template.loader import get_template
from django.shortcuts import render

from gestion_de_farmacias import settings

# importaciones necesarias para enviar emails
from django.conf import settings
from django.core.mail import send_mail

# Importacion de los Modelos
from gestionStock.models import Lotes, Medicamentos

# FORMULARIOS
from gestion_de_farmacias.forms import Formulario_nuevo_lote, Formulario_nuevo_medicamento


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


# ==============
# Medicamentos =
# ==============
def medicamentos(request):

    medicamentos = Medicamentos.objects.all()

    formulario_nuevo_medicamento = Formulario_nuevo_medicamento()

    diccionario_de_contexto = {"usuario": "Rafa Burgueño", "medicamentos": medicamentos,
                               'formulario_nuevo_medicamento': formulario_nuevo_medicamento}

    return render(request, "medicamentos.html", diccionario_de_contexto)


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


# ==================
# Nuevo medicamento =
# =================
def nuevo_medicamento(request):

    if request.method == "POST":
        formulario_nuevo_medicamento = Formulario_nuevo_medicamento(
            request.POST)

        if formulario_nuevo_medicamento.is_valid():

            nuevo_medicamento = formulario_nuevo_medicamento.cleaned_data

            # seguidamente hay que enviar los datos a la base de datos
            Medicamentos.objects.create(nuevo_medicamento)

            print("el request POST dice...")
            print(request.POST)
            print("datos para el nuevo medicamento...")
            print(nuevo_medicamento)

    else:
        formulario_nuevo_medicamento = Formulario_nuevo_medicamento()

    medicamentos = Medicamentos.objects.all()

    diccionario_de_contexto = {"usuario": "Rafaso", "medicamentos": medicamentos,
                               'formulario_nuevo_medicamento': formulario_nuevo_medicamento}

    return render(request, "medicamentos.html", diccionario_de_contexto)


# =======================================================================
# Stock =================================================================
# =====================================================================
"""
class StockList(ListView):
    model = Lotes

    template_name = 'stock.html'

class LoteCreate(CreateView):
    model = Lotes
    #fields = ['medicamento','stock','ubicacion','vencimiento']
    form_class = Formulario_lotes
    template_name = 'crear_stock.html'

    success_url=reverse_lazy('stock')
"""

def stock(request):

    # variables que se van a devolver
    diccionario_de_contexto = {}


    #================
    # Stock/busqueda =
    #================
    if request.GET.__contains__("termino_buscado"):
        print("ahora si llegan datos por GET al stock")
        # print(request.GET.__contains__("termino_buscado"))

        termino_buscado = request.GET["termino_buscado"]

        if len(termino_buscado) > 20:
            #mensaje = "El termino buscado es demasiado extenso."
            diccionario_de_contexto = {"mensaje": "El termino buscado es demasiado extenso.", }
        else:
            # __icontains busca la palabra en elguna parte del registro
            lotes_encontrados = Lotes.objects.filter(medicamento__icontains=termino_buscado)
            mensaje = "Se encontraron %r medicamentos" % len(lotes_encontrados)
            
            diccionario_de_contexto = {"lotes_encontrados": lotes_encontrados,"termino_buscado": termino_buscado, "mensaje": mensaje}

    #===========================
    # Stock / creacion de un lote =
    #===========================
    if request.method == "POST":
        print("si llegan datos por POST al stock")

        formulario_nuevo_stock = Formulario_nuevo_lote(request.POST)

        if formulario_nuevo_stock.is_valid():

            nuevo_stock = formulario_nuevo_stock.cleaned_data

            # seguidamente hay que enviar los datos a la base de datos
            print("datos para el nuevo stock...")
            print(nuevo_stock)

            # limpia el form para poder volver a la pagina
            formulario_nuevo_stock = Formulario_nuevo_lote()

    else:
        formulario_nuevo_stock = Formulario_nuevo_lote()

    # tabla de lotes existentes
    lotes_list = Lotes.objects.all()

    diccionario_de_contexto = {'lotes_list': lotes_list,
                               'formulario_nuevo_stock': formulario_nuevo_stock}

    return render(request, "stock.html", diccionario_de_contexto)






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
