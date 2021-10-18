from django.urls import path
from .views import ListaMedicamentos, DetalleView,ActualizarView, CreateMedicamentos, EliminarView, CreatePresentacion

urlpatterns = [

	path('medicamentos', ListaMedicamentos.as_view(), name = 'lista_medicamentos'),
	path('medicamentos/detalle', DetalleView.as_view(), name ='detalle_medicamentos'),
	path('medicamentos/actualizar', ActualizarView.as_view(), name ="actualizar_medicamentos"),
	path('medicamentos/agregar', CreateMedicamentos.as_view(), name='create_medicamentos'),
	path('medicamentos/eliminar', EliminarView.as_view(), name="eliminar_medicamentos"), 
	path('medicamentos/reporte/$', 'apps.medicamentos.views.generar_reporte_medicamentos',name='reporte'),
	#presentacion
	path('medicamentos/presentacion', CreatePresentacion.as_view(), name='create_presentacion'),
]
