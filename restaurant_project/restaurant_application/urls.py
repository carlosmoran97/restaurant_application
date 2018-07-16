from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = "restaurant"

urlpatterns = [

        #URL PARA CATEGORI PLATILLO

    url(r'^categoria_platillos/$', views.index_categoria_platillos, name='index_categoria_platillos'),
    url(r'^create_categoria_platillos/$', login_required(views.CategoriaPlatilloCreate.as_view()), name='create_categoria_platillos'),
    url(r'^lista_categoria_platillos/$', login_required(views.CategoriaPlatilloList.as_view()), name='lista_categoria_platillos'),
    url(r'^editar_categoria_platillos/$', login_required(views.CategoriaPlatilloUpdate.as_view()), name='editar_categoria_platillos'),
    url(r'^eliminar_categoria_platillos/$', login_required(views.CategoriaPlatilloDelete.as_view()), name='eliminar_categoria_platillos'),


        #URL PARA PLATILLOS

    url(r'^platillos/$', views.index_platillos, name='index_platillos'),
    url(r'^create_platillos/$', login_required(views.PlatilloCreate.as_view()), name='create_platillos'),
    url(r'^lista_platillos/$', login_required(views.PlatilloList.as_view()), name='lista_platillos'),
    url(r'^editar_platillos/$', login_required(views.PlatilloUpdate.as_view()), name='editar_platillos'),
    url(r'^eliminar_platillos/$', login_required(views.PlatilloDelete.as_view()), name='eliminar_platillos'),

        #URL PARA MESAS

    url(r'^mesas/$', views.index_mesas, name='index_mesas'),
    url(r'^create_mesas/$', login_required(views.MesaCreate.as_view()), name='create_mesas'),
    url(r'^lista_mesas/$', login_required(views.MesaList.as_view()), name='lista_mesas'),
    url(r'^editar_mesas/$', login_required(views.MesaUpdate.as_view()), name='editar_mesas'),
    url(r'^eliminar_mesas/$', login_required(views.MesaDelete.as_view()), name='eliminar_mesas'),

        #URL PARA EMPLEADOS

    url(r'^empleados/$', views.index_empleados, name='index_empleados'),
    url(r'^create_empleado/$', login_required(views.EmpleadoCreate.as_view()), name='create_empleado'),
    url(r'^lista_empleados/$', login_required(views.EmpleadosList.as_view()), name='lista_empleados'),
    url(r'^detalle_empleado/$', login_required(views.EmpleadoDetalle.as_view()), name='detalle_empleado'),
    url(r'^editar_empleado/$', login_required(views.EmpleadoUpdate.as_view()), name='editar_empleado'),
    url(r'^eliminar_empleado/$', login_required(views.EmpleadoDelete.as_view()), name='eliminar_empleado'),
]
