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

# importaciones necesarias para enviar emails
from django.conf import settings
from django.core.mail import send_mail




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
    #print("el request.user.rol.nombre dice: " + str(request.user.rol.nombre) )
    # json_personas= json.dumps(lista_personas)
    # json_personas= json.dumps([11,12,13,14,15])
    json_personas = [11, 12, 13, 14, 15]

    diccionario_de_contexto = {
        "datos_json": json_personas, "usuario": "Rafael Burgueño"}

    return render(request, "inicio.html", diccionario_de_contexto)







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


