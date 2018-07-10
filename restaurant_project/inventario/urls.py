from django.conf.urls import url
from inventario import views

app_name = 'inventario'

urlpatterns = [
    url(r'^productos/$', views.productos, name='productos'),
    url(r'^productos_list/$', views.Get_producto_List.as_view(), name='productos_list'),
    url(r'^productos_filter/$', views.Get_producto_ListFilter.as_view(), name='productos_filter'),
    url(r'^productos_create/$', views.Get_producto_Create.as_view(), name='productos_create'),
    url(r'^productos_update/$', views.Get_producto_Update.as_view(), name='productos_update'),
    url(r'^productos_delete/$', views.Get_producto_Delete.as_view(), name='productos_delete'),
]