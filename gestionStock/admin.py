from django.contrib import admin

# Register your models here.
from gestionStock.models import Medicamentos, Lotes, Farmacias

admin.site.register(Medicamentos)
admin.site.register(Lotes)
admin.site.register(Farmacias)

