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
    #url(r'^listafilter_categoria_platillos/$', views.CategoriaPlatilloListFilter.as_view(), name='listafilter_categoria_platillos'),
    url(r'^editar_platillos/$', views.PlatilloUpdate.as_view(), name='editar_platillos'),
    url(r'^eliminar_platillos/$', views.PlatilloDelete.as_view(), name='eliminar_platillos'),
]
