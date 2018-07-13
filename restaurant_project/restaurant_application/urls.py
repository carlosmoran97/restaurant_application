from django.conf.urls import url
from . import views

app_name = "restaurant"

urlpatterns = [

        #URL PARA CATEGORI PLATILLO

    url(r'^categoria_platillos/$', views.index_categoria_platillos, name='index_categoria_platillos'),
    url(r'^create_categoria_platillos/$', views.CategoriaPlatilloCreate.as_view(), name='create_categoria_platillos'),
    url(r'^lista_categoria_platillos/$', views.CategoriaPlatilloList.as_view(), name='lista_categoria_platillos'),
    url(r'^editar_categoria_platillos/$', views.CategoriaPlatilloUpdate.as_view(), name='editar_categoria_platillos'),
    url(r'^eliminar_categoria_platillos/$', views.CategoriaPlatilloDelete.as_view(), name='eliminar_categoria_platillos'),


        #URL PARA PLATILLOS

    url(r'^platillos/$', views.index_platillos, name='index_platillos'),
    url(r'^create_platillos/$', views.PlatilloCreate.as_view(), name='create_platillos'),
    url(r'^lista_platillos/$', views.PlatilloList.as_view(), name='lista_platillos'),
    url(r'^editar_platillos/$', views.PlatilloUpdate.as_view(), name='editar_platillos'),
    url(r'^eliminar_platillos/$', views.PlatilloDelete.as_view(), name='eliminar_platillos'),

        #URL PARA MESAS

    url(r'^mesas/$', views.index_mesas, name='index_mesas'),
    url(r'^create_mesas/$', views.MesaCreate.as_view(), name='create_mesas'),
    url(r'^lista_mesas/$', views.MesaList.as_view(), name='lista_mesas'),
    url(r'^editar_mesas/$', views.MesaUpdate.as_view(), name='editar_mesas'),
    url(r'^eliminar_mesas/$', views.MesaDelete.as_view(), name='eliminar_mesas'),

        #URL PARA EMPLEADOS

    url(r'^empleados/$', views.index_empleados, name='index_empleados'),
    url(r'^create_empleado/$', views.EmpleadoCreate.as_view(), name='create_empleado'),
    url(r'^lista_empleados/$', views.EmpleadosList.as_view(), name='lista_empleados'),
    url(r'^detalle_empleado/$', views.EmpleadoDetalle.as_view(), name='detalle_empleado'),
    url(r'^editar_empleado/$', views.EmpleadoUpdate.as_view(), name='editar_empleado'),
    url(r'^eliminar_empleado/$', views.EmpleadoDelete.as_view(), name='eliminar_empleado'),
]
