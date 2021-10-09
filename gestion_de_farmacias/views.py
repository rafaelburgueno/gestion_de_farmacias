#from django.http import HttpResponse
#from django.views.generic.base import TemplateView
#from django.template import Template, Context
#import datetime
#import os
#import json
#from django.template.loader import get_template
from django.shortcuts import render



#===============================================================
# funciones que dan respuesta a las peticion provenientes de urls.py  =
#===============================================================


#========
# Inicio =
#========
def inicio(request):

	lista_personas=[{
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

	#json_personas= json.dumps(lista_personas)
	#json_personas= json.dumps([11,12,13,14,15])
	json_personas= [11,12,13,14,15]


	diccionario_de_contexto={"datos_json":json_personas,"usuario":"Rafael Burgueño"}

	return render(request, "inicio.html", diccionario_de_contexto)




#=======
# Stock =
#=======
def stock(request):

	diccionario_de_contexto={"usuario":"Rafael Burgueño"}

	return render(request, "stock.html", diccionario_de_contexto)





#=======
# Login =
#=======
def login(request):

	diccionario_de_contexto={"usuario":"Rafael Burgueño"}

	return render(request, "login.html", diccionario_de_contexto)





#=========
# Recetas =
#=========
#def receta(request, receta_numero,usuario):
def recetas(request):

	recetas=["receta 1","receta 2","receta 3","receta 4"]

	diccionario_de_contexto={"usuario":"Rafael Burgueño", "recetas":recetas}

	return render(request, "recetas.html", diccionario_de_contexto)





#=========
# Usuario =
#=========
def usuario(request):

	diccionario_de_contexto={"usuario":"Rafael Burgueño"}

	return render(request, "usuario.html", diccionario_de_contexto)
