from django.conf.urls import url
from procesos import views

app_name = 'procesos'

urlpatterns = [
    url(r'^usuarios/', views.registro_usuario, name='registro_usuarios'),
    url(r'^sesion_caja/', views.sesion_caja, name='sesion_caja'),
    url(r'^create_sesion_caja/', views.CreateSesionCaja.as_view(), name='create_sesion_caja'),
    url(r'^cerrar_sesion_caja/', views.CerrarSesionCaja.as_view(), name='cerrar_sesion_caja'),
    url(r'^lista_sesion_caja/', views.SesionList.as_view(), name='lista_sesion_caja'),
    url(r'^detalle_sesion_caja/', views.DetalleSesionCaja.as_view(), name='detalle_sesion_caja'),
    # urls utiles para realizar ordenes
    url(r'^panel_mesas/', views.PanelMesasView.as_view(), name='panel_mesas'),
]
