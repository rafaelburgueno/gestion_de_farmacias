from django.urls import path
from gestionUsuarios import views

app_name = "gestionUsuarios"

urlpatterns = [
    path('', views.base, name="base"),
    #path('home', views.home, name="home"),
    path('gestionUsuarios', views.usuarios, name="usuarios"),
    
]
