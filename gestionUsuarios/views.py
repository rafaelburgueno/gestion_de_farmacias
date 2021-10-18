from django.shortcuts import render, redirect
from gestionUsuarios.models import *
from gestionUsuarios.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db import connection
import subprocess, shlex
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.

def index(request):
    return render(request, "usuarios/index.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "¡Nuevo usuario creado! Por favor, registrese.")
            return redirect('usuarios:index')
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})

@login_required
def home(request):
    return render(request, "usuarios/home.html")

@login_required
def usuarios(request):
    if request.method == "POST":
        identificador = request.POST.get("usuario_id")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        edad = request.POST.get("edad")
        sexo = request.POST.get("sexo")
        departmento = request.POST.get("departmento")
        

        
        Usuario.objects.create(identificador=id, nombre=nombre, apellido=apellido,
        edad=edad, sexo=sexo, departmento=departmento)

        
        return redirect("usuarios:usuarios")
    else:
        # Fetch all employees using Django ORM
        usuarios = Usuario.objects.all()

        return render(request, 'usuarios/index.html',
        {"usuarios":usuarios})


