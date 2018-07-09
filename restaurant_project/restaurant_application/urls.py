from django.conf.urls import url
from . import views

app_name = "restaurant"

urlpatterns = [
    url(r'^categoria_platillos/$', views.index_categoria_platillos, name='index_categoria_platillos'),
]
