from django.conf.urls import url
from procesos import views

app_name = 'procesos'

urlpatterns = [
    url('^usuarios/', views.registro_usuario, name='registro_usuarios'),
    url('^sesion_caja/', views.sesion_caja, name='sesion_caja'),
    url('^create_sesion_caja/', views.CreateSesionCaja.as_view(), name='create_sesion_caja'),
    url('^cerrar_sesion_caja/', views.CerrarSesionCaja.as_view(), name='cerrar_sesion_caja'),
    url('^lista_sesion_caja/', views.SesionList.as_view(), name='lista_sesion_caja'),
    url('^detalle_sesion_caja/', views.DetalleSesionCaja.as_view(), name='detalle_sesion_caja'),
]
