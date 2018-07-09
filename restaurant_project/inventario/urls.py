from django.conf.urls import url
from inventario import views

app_name = 'inventario'

urlpatterns = [
    url(r'^productos/$', views.productos, name='productos'),
    
]