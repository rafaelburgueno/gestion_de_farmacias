from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from gestionStock.models import Medicamentos

# segui las instrucciones de el video de youtube ...
# "54. Curso Django2: Usuario Personalizado - modelo" del canal Developer.pe, para implementar este modelo 





#==========
#Roles ====
#==========
class Roles(models.Model):
        #id= models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length = 50, unique = True)
        descripcion=models.CharField(max_length=200)

        def __str__(self):
                return str(self.nombre) + " " + str(self.descripcion)





#==========
# Usuarios =
#==========
class Usuarios(AbstractBaseUser):
        cedula_de_identidad = models.IntegerField(primary_key=True,verbose_name="c.i." , help_text='Para todo usuario es el numero de CI')
        
        rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
        usuario = models.CharField(max_length = 20, unique=True, verbose_name="Nombre de usuario")
        password = models.CharField(max_length = 100)

        nombre = models.CharField(max_length = 100)
        apellido = models.CharField(max_length = 100)
        usuario_activo = models.BooleanField(default=True)
        usuario_administrador = models.BooleanField(default=False)
        sexo = models.CharField(max_length = 50, blank=True, null=True)
        fecha_de_nacimiento= models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
        departmento = models.CharField(max_length = 50, blank=True, null=True)
        direccion=models.CharField(max_length=200, blank=True, null=True)
        telefono=models.IntegerField(blank=True, null=True)
        email=models.EmailField()
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
        updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


        


        def __str__(self):
                return self.usuario
        
        def has_perm(self,perm,obj = None):
                return True

        def has_module_perms(self, app_label):
                return True

        @property
        def is_staff(self):
                return self.usuario_administrador





#==========
# Recetas =
#==========
class Recetas(models.Model):
        #id = models.IntegerField(primary_key=True)
        
        medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
        paciente = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE, related_name='+')
        medico = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE, related_name='+')

        descripcion = models.CharField(max_length = 500, blank=True, null=True)
        vencimiento= models.DateField(blank=True, null=True, verbose_name="Fecha de vencimiento")
        estado = models.CharField(max_length = 50) # el estado se refiere a si el medicamento esta reservado o ya fue retirado
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
        updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

        

        def __str__(self):
                return "Se receta " + str(self.medicamento) + " al usuario " +str(self.paciente)