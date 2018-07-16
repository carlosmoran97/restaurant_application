from django.conf.urls import url
from procesos import views
from django.contrib.auth.decorators import login_required

app_name = 'procesos'

urlpatterns = [
    url(r'^usuarios/', login_required(views.registro_usuario), name='registro_usuarios'),
    url(r'^sesion_caja/', login_required(views.sesion_caja), name='sesion_caja'),
    url(r'^create_sesion_caja/', login_required(views.CreateSesionCaja.as_view()), name='create_sesion_caja'),
    url(r'^cerrar_sesion_caja/', login_required(views.CerrarSesionCaja.as_view()), name='cerrar_sesion_caja'),
    url(r'^lista_sesion_caja/', login_required(views.SesionList.as_view()), name='lista_sesion_caja'),
    url(r'^detalle_sesion_caja/', login_required(views.DetalleSesionCaja.as_view()), name='detalle_sesion_caja'),
    # urls utiles para realizar ordenes
    url(r'^panel_mesas/', login_required(views.PanelMesasView.as_view()), name='panel_mesas'),
    url(r'^abrir_orden/', login_required(views.AbrirOrden.as_view()), name='abrir_orden'),
    url(r'^detalle_orden/(?P<pk>\d+)/$', login_required(views.detalle_orden.as_view()), name='detalle_orden'),
    url(r'^orden_detail/', login_required(views.OrdenDetail.as_view()), name='orden_detail'),
]
