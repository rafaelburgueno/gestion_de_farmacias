"""gestion_de_farmacias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from gestion_de_farmacias.views import login, inicio
from gestion_de_farmacias import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
    path('medicamentos/', views.medicamentos, name="medicamentos"),
    #path('medicamentos/', views.MedicamentosListView.as_view(), name="medicamentos"),
    path('buscar_medicamento/', views.buscar_medicamento, name="buscar_medicamento"),
    path('nuevo_medicamento/', views.nuevo_medicamento, name="nuevo_medicamento"),

    #path('stock/', views.stock, name="stock"),
    path('stock/', views.StockList.as_view(), name="stock"),

    #path('receta/<int:receta_numero>/<str:usuario>', views.receta, name="receta"),
    path('recetas/', views.recetas, name="recetas"),
    #path('enviar_receta/', views.enviar_receta, name="enviar_receta"),

    path('usuario/', views.usuario, name="usuario"),
    #path('login/', views.login, name="login"),
    path('login/', views.LoginPageView.as_view(), name="login"),


]
