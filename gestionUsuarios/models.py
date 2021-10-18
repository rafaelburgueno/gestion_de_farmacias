from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)

# Create your models here.

class usuarios(models.Model):
   
    identificador = models.IntegerField(primary_key=True,help_text='Para todo usuario es el numero de CI')
    nombre = models.CharField(max_length = 1000)
    apellido = models.CharField(max_length = 1000)
    edad = models.IntegerField()
    sexo = models.CharField(max_length = 100)
    departmento = models.CharField(max_length = 1000)
    fechadenac= models.CharField(max_length = 1000)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.first_name

class Usuario(AbstractUser):
    nombre = models.CharField(max_length = 1000)
    apellido = models.CharField(max_length = 1000)
    edad = models.IntegerField()
    identificador = models.BigIntegerField(primary_key=True, help_text='Para todo usuario es el numero de CI')
    email = models.EmailField(verbose_name='correo electronico', max_length=100)
    direccion = models.CharField(max_length=100, null=True, blank=True, help_text='Direccion')
    telefono = models.CharField(max_length=50, null=True, blank=True, help_text='Telefono Fijo')
    celular = models.CharField(max_length=50, help_text='Celular')
    opciones_tipo_usuarios = (
            
            ('Usuario', 'Usuario'),
            ('Funcionario', 'Funcionario'),
            ('Administrador', 'Administrador'),
        )
    tipo_usuario = models.CharField(max_length=20, choices=opciones_tipo_usuarios, default='Usuario', help_text='Tipo de Usuario') 

    

    

    