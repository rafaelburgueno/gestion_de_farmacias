
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from gestionStock.models import Medicamentos

# segui las instrucciones de el video de youtube ...
# "54. Curso Django2: Usuario Personalizado - modelo" del canal Developer.pe, para implementar este modelo 


class UsuarioManager(BaseUserManager):
        
        def create_user(self, email, usuario, nombre, apellido, password = None):
                if not email:
                        raise ValueError('El usuario debe tener un correo electronico!')

                usuario = self.model(
                        usuario = usuario, 
                        email = self.normalize_email(email), 
                        nombre = nombre, 
                        apellido = apellido
                )

                usuario.set_password(password)

                usuario.save()
                return usuario
        
        
        def create_superuser(self, usuario, email, nombre, apellido, password):
                usuario = self.create_user(
                        email, 
                        usuario = usuario, 
                        nombre = nombre, 
                        apellido = apellido
                )
                usuario.usuario_administrador = True
                usuario.save()
                return usuario




#==========
#Roles ====
#==========
class Roles(models.Model):
        #id= models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length = 50, unique = True)
        descripcion=models.CharField(max_length=200,blank=True, null=True)

        def __str__(self):
                return str(self.nombre) + " " + str(self.descripcion)

        class Meta:
                verbose_name = "Rol"
                verbose_name_plural = "Roles"
                ordering = ["nombre"]



#==========
# Usuarios =
#==========
class Usuarios(AbstractBaseUser):
        cedula_de_identidad = models.IntegerField(primary_key=True,verbose_name="c.i." , help_text='Para todo usuario es el numero de c.i.')
        
        rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
        usuario = models.CharField(max_length = 100, unique=True, verbose_name="Nombre de usuario")
        #password = models.CharField(max_length = 100)

        nombre = models.CharField(max_length = 100,blank=True, null=True)
        apellido = models.CharField(max_length = 100,blank=True, null=True)
        usuario_activo = models.BooleanField(default=True)
        usuario_administrador = models.BooleanField(default=False)
        sexo = models.CharField(max_length = 50, blank=True, null=True)
        fecha_de_nacimiento= models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
        departmento = models.CharField(max_length = 50, blank=True, null=True)
        direccion=models.CharField(max_length=200, blank=True, null=True)
        telefono=models.IntegerField(blank=True, null=True)
        email=models.EmailField(blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
        updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

        objects = UsuarioManager()

        USERNAME_FIELD = 'usuario'
        REQUIRED_FIELDS = ['nombre','apellido']



        def __str__(self):
                return self.usuario
        
        def has_perm(self,perm,obj = None):
                return True

        def has_module_perms(self, app_label):
                return True

        @property
        def is_staff(self):
                return self.usuario_administrador

        class Meta:
                verbose_name = "Usuario"
                verbose_name_plural = "Usuarios"
                ordering = ["usuario"]



#==========
# Recetas =
#==========
class Recetas(models.Model):
        ESTADOS_DE_UNA_RECETA = [
                ('RES', 'Reservado'),
                ('RET','Retirado')
        ]

        #id = models.IntegerField(primary_key=True)
        
        medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
        paciente = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE, related_name='+')
        medico = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE, related_name='+')

        descripcion = models.CharField(max_length = 500, blank=True, null=True)
        vencimiento= models.DateField(blank=True, null=True, verbose_name="Fecha de vencimiento")
        estado = models.CharField(max_length = 50,choices=ESTADOS_DE_UNA_RECETA,blank=True, null=True) # el estado se refiere a si el medicamento esta reservado o ya fue retirado
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
        updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

        

        def __str__(self):
                return "Se receta " + str(self.medicamento) + " al usuario " +str(self.paciente)


        class Meta:
                verbose_name = "Receta"
                verbose_name_plural = "Recetas"
                ordering = ["paciente"]