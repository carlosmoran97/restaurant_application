from django.conf.urls import url
from inventario import views
from django.contrib.auth.decorators import login_required
app_name = 'inventario'

urlpatterns = [
    # urls del api rest para el crud de producto
    url(r'^productos/$', views.productos, name='productos'),
    url(r'^productos_list/$', login_required(views.Get_producto_List.as_view()), name='productos_list'),
    url(r'^productos_filter/$', login_required(views.Get_producto_ListFilter.as_view()), name='productos_filter'),
    url(r'^productos_create/$', login_required(views.Get_producto_Create.as_view()), name='productos_create'),
    url(r'^productos_update/$', login_required(views.Get_producto_Update.as_view()), name='productos_update'),
    url(r'^productos_delete/$', login_required(views.Get_producto_Delete.as_view()), name='productos_delete'),
    # urls de las vistas basadas en clases para los reportes de inventario
    url(r'^reportes/$', login_required(views.ReporteDeExistenciaList.as_view()), name='reportes'),
    url(r'^reportes/(?P<pk>\d+)/$', login_required(views.ReporteDeExistenciaDetail.as_view()), name='reporte_detail'),
    url(r'^reportes/(?P<pk>\d+)/pdf', login_required(views.pdf_view.as_view()), name='reporte_detail_pdf'),
    url(r'^reportes/create/$', login_required(views.ReporteDeExistenciaCreateView.as_view()), name='reporte_create'),
    url(r'^reportes/update/(?P<pk>\d+)/$', login_required(views.ReporteDeExistenciaUpdateView.as_view()), name='reporte_update'),
    url(r'^reportes/delete/(?P<pk>\d+)/$', login_required(views.ReporteDeExistenciaDeleteView.as_view()), name='reporte_delete'),
    # urls del api rest para el crud de existencias
    url(r'^existencias_list/$', login_required(views.GetExistenciasList.as_view()), name='existencias_list'),
    url(r'^existencias_create/$', login_required(views.GetExistenciasCreate.as_view()), name='existencias_create'),
    url(r'^existencias_delete/$', login_required(views.GetExistenciasDelete.as_view()), name='existencias_delete'),
    url(r'^existencias_update/$', login_required(views.GetExistenciasUpdate.as_view()), name='existencias_update'),
]