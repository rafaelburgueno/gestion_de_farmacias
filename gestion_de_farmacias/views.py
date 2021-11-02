from django.db.models.query import QuerySet
from django.http import HttpResponse

# vistas basadas en clases
from django.views.generic import TemplateView, ListView, CreateView, View, UpdateView

from gestionStock.models import Medicamentos
from gestionUsuarios.models import Usuarios

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

    #print("el request.user.rol.nombre dice: " + str(request.user.rol.nombre) )

    diccionario_de_contexto = {"usuario": "Rafael Burgueño"}

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





# ===============================
# Carga de datos a la base de datos =
# ===============================
def carga_medicamentos(request):

    for medicamento in MEDICAMENTOS:
        #print("si lee el array")
        print("-->" + str(medicamento["nombre_comercial"]))
        
        medicamento_nuevo = Medicamentos.objects.create(
            nombre_comercial=medicamento["nombre_comercial"], 
            categoria='venta libre', 
            laboratorio=medicamento["laboratorio"], 
            principio_activo=medicamento["nombre_comercial"], 
            forma="comprimidos", 
            contraindicaciones=medicamento["contraindicaciones"]
        )
    
        medicamento_nuevo.save()

    """
     medicamento_nuevo = Medicamentos.objects.create(
            nombre_comercial=medicamento["nombre_comercial"], 
            categoria='venta libre', 
            laboratorio=medicamento["nombre_comercial"], 
            principio_activo=medicamento["nombre_comercial"], 
            forma=medicamento["nombre_comercial"], 
            contraindicaciones=medicamento["nombre_comercial"]

    
    """

    #print("paso por la funcion carga_datos")

    return redirect('medicamentos')



"""
###################################################################
plantilla para generar los datos en: https://www.json-generator.com/
###################################################################
[
  '{{repeat(5, 7)}}',
  {
    nombre_comercial: '{{surname()}}{{integer(100, 999)}}',
    laboratorio: '{{company().toUpperCase()}}',
    contraindicaciones: '{{lorem(1, "paragraphs")}}'
  }
]
"""

MEDICAMENTOS= [
  {
    "nombre_comercial": "Young165",
    "laboratorio": "BITENDREX",
    "contraindicaciones": "Tempor aliqua ullamco est dolore ea. Laborum adipisicing fugiat est reprehenderit occaecat anim fugiat occaecat aute ad irure voluptate sunt. Reprehenderit aute incididunt elit est nulla mollit cupidatat amet.\r\n"
  },
  {
    "nombre_comercial": "Poole701",
    "laboratorio": "XTH",
    "contraindicaciones": "Cupidatat elit in ad elit anim qui ex eu. Nostrud deserunt ipsum nulla quis commodo culpa cillum consequat veniam. Tempor nisi sit mollit laboris irure dolore cupidatat amet.\r\n"
  },
  {
    "nombre_comercial": "Mcpherson865",
    "laboratorio": "THREDZ",
    "contraindicaciones": "Fugiat id minim aliquip sunt in commodo. Sint exercitation amet consectetur culpa incididunt sit mollit sint tempor proident sit in est occaecat. Sint do in amet commodo eu dolor quis aliqua id ipsum id proident id.\r\n"
  },
  {
    "nombre_comercial": "Bright795",
    "laboratorio": "ROBOID",
    "contraindicaciones": "Nulla cupidatat deserunt officia minim aliqua culpa amet non laboris. Magna consectetur eu ullamco laboris aliquip irure consequat aute nisi in elit anim. Sunt irure pariatur id ea id aute. Ut eiusmod fugiat incididunt cillum officia nulla excepteur incididunt proident ipsum labore. Mollit cillum irure mollit eu consequat. Enim sit est exercitation Lorem exercitation qui aliquip et pariatur amet occaecat eiusmod.\r\n"
  },
  {
    "nombre_comercial": "Rivera355",
    "laboratorio": "COLLAIRE",
    "contraindicaciones": "Exercitation dolor id duis elit ad excepteur nisi deserunt tempor occaecat proident. Lorem qui cillum proident ut consectetur elit laboris consequat qui. Laborum nulla irure anim eiusmod id nisi eiusmod duis adipisicing consectetur Lorem eiusmod ipsum. Nisi cupidatat in minim nulla sunt amet veniam enim deserunt voluptate. Do ipsum ad magna ea sint.\r\n"
  },
  {
    "nombre_comercial": "Stuart598",
    "laboratorio": "REALYSIS",
    "contraindicaciones": "Deserunt dolore voluptate exercitation sit dolore sit pariatur velit ut id in magna tempor mollit. Aute veniam ex commodo consequat incididunt dolor aliqua dolore exercitation laboris enim. Voluptate mollit ut minim occaecat et labore reprehenderit elit esse.\r\n"
  },
  {
    "nombre_comercial": "Newman212",
    "laboratorio": "NETBOOK",
    "contraindicaciones": "Mollit consequat enim anim aliqua sint. Nulla sunt tempor ullamco ullamco elit non eiusmod velit eu qui do. Aute sint laboris sit ut consequat exercitation in eiusmod.\r\n"
  },
  {
    "nombre_comercial": "Winters413",
    "laboratorio": "BITTOR",
    "contraindicaciones": "Enim et deserunt ipsum aliquip consequat non. Esse amet eu laborum incididunt laborum amet magna sit eu incididunt pariatur proident elit esse. Velit et cupidatat labore enim exercitation exercitation labore ea do irure elit eiusmod elit incididunt. Aliqua in occaecat voluptate id duis occaecat eu. Duis dolore exercitation pariatur exercitation nisi Lorem. Aliquip irure nisi reprehenderit occaecat aliquip enim occaecat ut duis. Nostrud sunt ad ex officia dolor id ipsum do.\r\n"
  },
  {
    "nombre_comercial": "Wade360",
    "laboratorio": "CONFRENZY",
    "contraindicaciones": "Esse et in eu laboris culpa ex ut et. Velit mollit adipisicing sit pariatur dolore in magna magna laborum cupidatat. Occaecat amet qui est ut in et Lorem esse magna nulla. Reprehenderit proident aute proident amet do.\r\n"
  },
  {
    "nombre_comercial": "Gates944",
    "laboratorio": "COGENTRY",
    "contraindicaciones": "Do aute irure quis pariatur mollit velit ipsum. Reprehenderit duis adipisicing mollit magna. Nostrud id velit aliquip laboris non voluptate culpa et proident quis eu ut. Lorem aliqua duis esse sit ipsum in laborum ea id officia adipisicing ullamco exercitation.\r\n"
  },
  {
    "nombre_comercial": "Fox342",
    "laboratorio": "ECSTASIA",
    "contraindicaciones": "Officia reprehenderit pariatur ullamco elit dolor excepteur ullamco anim occaecat Lorem et reprehenderit excepteur esse. Pariatur reprehenderit irure elit exercitation. Cillum et qui et officia incididunt in duis aliqua. Culpa veniam adipisicing laborum labore est. Occaecat magna laborum Lorem cupidatat culpa est laborum eiusmod tempor.\r\n"
  },
  {
    "nombre_comercial": "Humphrey186",
    "laboratorio": "UTARIAN",
    "contraindicaciones": "Ea nostrud commodo officia magna commodo fugiat. Velit qui duis non exercitation minim sint cillum Lorem et. Irure irure occaecat nulla magna. Ut ipsum id eiusmod cillum magna aliquip veniam amet aliquip deserunt qui reprehenderit minim do. Qui cillum laboris cupidatat consectetur elit dolor ullamco non irure qui ad duis. Consequat qui consequat sit amet esse exercitation.\r\n"
  },
  {
    "nombre_comercial": "Harvey401",
    "laboratorio": "ACCUFARM",
    "contraindicaciones": "Irure laborum labore consequat irure non. Reprehenderit commodo dolor exercitation occaecat reprehenderit ipsum pariatur excepteur Lorem ullamco elit ut quis ea. Sint consequat proident proident amet ipsum minim nisi cillum ad. Aute sunt adipisicing minim ea non labore do adipisicing irure consequat elit culpa.\r\n"
  },
  {
    "nombre_comercial": "Davenport305",
    "laboratorio": "ANDRYX",
    "contraindicaciones": "Dolore cillum incididunt irure eiusmod veniam consectetur amet et magna proident in aute proident. Ut minim cillum consequat nulla. Laborum fugiat enim est incididunt dolore tempor ea in reprehenderit. Voluptate excepteur ex duis nulla. Id aute sint incididunt ipsum fugiat.\r\n"
  },
  {
    "nombre_comercial": "Mcintyre728",
    "laboratorio": "URBANSHEE",
    "contraindicaciones": "Minim labore sunt laborum velit dolor occaecat aliquip pariatur reprehenderit excepteur aute quis. Reprehenderit ex excepteur ullamco deserunt. Et pariatur est eu sit do. Duis nostrud ullamco magna voluptate nostrud.\r\n"
  },
  {
    "nombre_comercial": "Knapp419",
    "laboratorio": "QUOTEZART",
    "contraindicaciones": "Eiusmod incididunt duis exercitation sint labore occaecat nostrud. Tempor elit reprehenderit minim elit qui ex. Et sunt sit fugiat qui ea enim reprehenderit. Sit eiusmod laboris cupidatat nisi Lorem et proident exercitation qui ad nisi incididunt. Pariatur nostrud ea id sint aliquip occaecat sit dolore laborum fugiat irure. Fugiat eiusmod ea reprehenderit tempor aute ipsum. Eu ad commodo sit proident nulla adipisicing incididunt ad aliquip officia ut tempor.\r\n"
  },
  {
    "nombre_comercial": "Velez656",
    "laboratorio": "MEDESIGN",
    "contraindicaciones": "Sint elit proident do excepteur consequat culpa enim sint amet. Proident in do pariatur sit ullamco. Velit cillum qui velit minim mollit non enim cillum do magna velit. Amet voluptate duis consectetur nulla duis eiusmod id nostrud sint occaecat ullamco ullamco ut magna. Cillum incididunt laboris mollit veniam ea mollit.\r\n"
  },
  {
    "nombre_comercial": "Greer919",
    "laboratorio": "CYCLONICA",
    "contraindicaciones": "Cillum consequat nulla ex cupidatat. Aliqua quis reprehenderit anim consectetur eu nostrud sint qui nulla voluptate magna occaecat. Reprehenderit laborum veniam quis laborum cillum amet laboris ea pariatur.\r\n"
  },
  {
    "nombre_comercial": "Conrad572",
    "laboratorio": "IMKAN",
    "contraindicaciones": "Deserunt deserunt sunt nisi laborum eu do magna exercitation adipisicing. Ex elit mollit est labore labore dolore enim eiusmod in veniam anim id. Adipisicing eu nostrud ullamco ea do. Eiusmod quis excepteur ipsum est deserunt excepteur duis. Tempor officia Lorem laboris est officia est ut do aute occaecat consequat.\r\n"
  },
  {
    "nombre_comercial": "Wise511",
    "laboratorio": "TSUNAMIA",
    "contraindicaciones": "Ut pariatur excepteur aliqua ex sit nostrud. Id eu deserunt est tempor fugiat nulla pariatur commodo. Ea labore eu eiusmod in. Amet enim velit non ad id voluptate laboris nostrud pariatur magna culpa. Ullamco sit proident excepteur fugiat aliquip do laboris labore enim consectetur.\r\n"
  }
]







# ===============================
# Carga Usuarios a la base de datos =
# ===============================
def carga_usuarios(request):

    for usuario in USUARIOS:
       
        usuario_nuevo = Usuarios.objects.create(
            cedula_de_identidad=usuario['cedula_de_identidad'], 
            #rol=usuario["rol"], 
            usuario=usuario["usuario"], 
            nombre=usuario["nombre"], 
            apellido=usuario["apellido"], 
            fecha_de_nacimiento=usuario["fecha_de_nacimiento"], 
            email=usuario["email"], 
            telefono=usuario["telefono"], 
            direccion=usuario["direccion"]
        )
    
        usuario_nuevo.save()


    print("paso por la funcion carga_usuaros")

    return redirect('lista_de_usuarios')


USUARIOS = [
  {
    "cedula_de_identidad": 19658412,
    "rol": 2,
    "usuario": "Price473",
    "nombre": "Becker",
    "apellido": "Rice",
    "fecha_de_nacimiento": "2018-11-13",
    "email": "beckerrice@shepard.com",
    "telefono": 95715696,
    "direccion": "488 Amboy Street, Longoria, Illinois, 4739"
  },
  {
    "cedula_de_identidad": 52347597,
    "rol": 2,
    "usuario": "Janelle751",
    "nombre": "Foster",
    "apellido": "Wiley",
    "fecha_de_nacimiento": "2004-12-31",
    "email": "fosterwiley@shepard.com",
    "telefono": 95751176,
    "direccion": "532 Bradford Street, Morgandale, Wisconsin, 6829"
  },
  {
    "cedula_de_identidad": 36957287,
    "rol": 2,
    "usuario": "Lila297",
    "nombre": "Etta",
    "apellido": "Hernandez",
    "fecha_de_nacimiento": "1987-08-01",
    "email": "ettahernandez@shepard.com",
    "telefono": 97570793,
    "direccion": "926 Bainbridge Street, Succasunna, Colorado, 2569"
  },
  {
    "cedula_de_identidad": 47058996,
    "rol": 3,
    "usuario": "Angie542",
    "nombre": "Maldonado",
    "apellido": "Lynn",
    "fecha_de_nacimiento": "1943-05-14",
    "email": "maldonadolynn@shepard.com",
    "telefono": 91238769,
    "direccion": "131 Micieli Place, Coalmont, Northern Mariana Islands, 6388"
  },
  {
    "cedula_de_identidad": 60358701,
    "rol": 3,
    "usuario": "Willa458",
    "nombre": "Marsha",
    "apellido": "Fox",
    "fecha_de_nacimiento": "1969-06-16",
    "email": "marshafox@shepard.com",
    "telefono": 95986899,
    "direccion": "935 Reed Street, Grayhawk, District Of Columbia, 3401"
  },
  {
    "cedula_de_identidad": 26115544,
    "rol": 3,
    "usuario": "Perez797",
    "nombre": "Mejia",
    "apellido": "Davenport",
    "fecha_de_nacimiento": "1946-05-20",
    "email": "mejiadavenport@shepard.com",
    "telefono": 98029617,
    "direccion": "486 Gold Street, Hebron, Kansas, 7066"
  },
  {
    "cedula_de_identidad": 47346714,
    "rol": 1,
    "usuario": "Kirby805",
    "nombre": "Nelda",
    "apellido": "Aguilar",
    "fecha_de_nacimiento": "1952-08-25",
    "email": "neldaaguilar@shepard.com",
    "telefono": 99991790,
    "direccion": "821 Lincoln Place, Wattsville, Montana, 6335"
  },
  {
    "cedula_de_identidad": 58213098,
    "rol": 3,
    "usuario": "Pansy702",
    "nombre": "Paul",
    "apellido": "Avila",
    "fecha_de_nacimiento": "1965-03-13",
    "email": "paulavila@shepard.com",
    "telefono": 97403485,
    "direccion": "550 Wogan Terrace, Glenbrook, Michigan, 8303"
  },
  {
    "cedula_de_identidad": 56227631,
    "rol": 2,
    "usuario": "Nola107",
    "nombre": "Green",
    "apellido": "Gilbert",
    "fecha_de_nacimiento": "1998-08-21",
    "email": "greengilbert@shepard.com",
    "telefono": 99460564,
    "direccion": "475 Fulton Street, Blodgett, Hawaii, 7332"
  },
  {
    "cedula_de_identidad": 24542962,
    "rol": 1,
    "usuario": "Olga791",
    "nombre": "Clarice",
    "apellido": "Yates",
    "fecha_de_nacimiento": "1993-10-01",
    "email": "clariceyates@shepard.com",
    "telefono": 91765033,
    "direccion": "664 Henry Street, Nicut, Puerto Rico, 2148"
  },
  {
    "cedula_de_identidad": 43383166,
    "rol": 3,
    "usuario": "Schneider199",
    "nombre": "Huber",
    "apellido": "Lewis",
    "fecha_de_nacimiento": "1967-11-12",
    "email": "huberlewis@shepard.com",
    "telefono": 96980160,
    "direccion": "969 Truxton Street, Bordelonville, Utah, 2301"
  },
  {
    "cedula_de_identidad": 20600421,
    "rol": 2,
    "usuario": "Valerie749",
    "nombre": "Mildred",
    "apellido": "Blackburn",
    "fecha_de_nacimiento": "1941-08-02",
    "email": "mildredblackburn@shepard.com",
    "telefono": 95504768,
    "direccion": "612 Lott Avenue, Ronco, Georgia, 7158"
  }
]


"""
###################################################################
plantilla para generar los datos en: https://www.json-generator.com/
###################################################################
 [
  '{{repeat(7, 20)}}',
  {
    cedula_de_identidad:'{{integer(10000000, 70000000)}}',
    rol:'{{integer(1, 3)}}',
    usuario: '{{firstName()}}{{integer(100, 999)}}',
    nombre: '{{firstName()}}',
    apellido: '{{surname()}}',
    fecha_de_nacimiento: '{{date(new Date(1940, 0, 1), new Date(), "YYYY-MM-dd")}}',
    email: '{{email()}}',
    telefono: '09{{integer(1000000, 9999999)}}',
    direccion: '{{integer(100, 999)}} {{street()}}, {{city()}}, {{state()}}, {{integer(100, 10000)}}'
  }
]
"""