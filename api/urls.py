from django.urls import path
from api import views

urlpatterns = [
    path('archivos',views.lista_archivos),
    path('compilar',views.compilar),
    path('crearArchivo',views.guardarArchivo),
    path('actualizarArchivo', views.actualizarArchivo),
    path('eliminarArchivo/<int:pk>',views.eliminarArchivo),
]