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
    url(r'^orden_condetalles_detail/', login_required(views.OrdenConDetallesDetailList.as_view()), name='orden_condetalle_detail'),
    url(r'^lista_ordenes/', login_required(views.GetOrdenesList.as_view()), name='orden_list'),
    url(r'^lista_ordenesporestado', login_required(views.GetOrdenesPorEstadoList.as_view()), name='orden_porestado_list'),
    url(r'^ordenes_activas', login_required(views.OrdenesActivas.as_view()), name='ordenes_activas'),
    url(r'^orden_update', login_required(views.GetOrdenesUpdate.as_view()), name='orden_update'),
    url(r'^orden_id', login_required(views.OrdenPago.as_view()), name="orden_id"),
    url(r'^lista_perfiles', login_required(views.PerfilDeUsuarioList.as_view()), name="lista_perfiles"),
    # urls utiles para realizar detalle de orden
    url(r'^create_detalle_orden', login_required(views.CreateDetalleOrden.as_view()), name='create_detalle_orden'),
    url(r'^update_detalle_orden', login_required(views.UpdateDetalleOrden.as_view()), name='update_detalle_orden'),
    url(r'^delete_detalle_orden', login_required(views.DeleteDetalleOrden.as_view()), name='delete_detalle_orden'),
    url(r'^detail_detalle_orden', login_required(views.DetalleOrdenDetail.as_view()), name='detail_detalle_orden'),
    # facturar
    url(r'^facturar', login_required(views.FacturarView.as_view()), name='facturar'),
    url(r'^detail_orden_mesa', login_required(views.OrdenDetailMesa.as_view()), name='detail_orden_mesa'),
    url(r'^pago/(?P<pk>\d+)/$', login_required(views.PagoView.as_view()), name="pago"),
    url(r'^pago/(?P<pk>\d+)/pdf/$', login_required(views.FacturaView.as_view()), name="factura_pdf"),
    url(r'^create_pago', login_required(views.GetCreatePago.as_view()), name="create_pago"),
    # historial de ordenes
    url(r'^historial', login_required(views.HistorialList.as_view()), name='historial'),
]
