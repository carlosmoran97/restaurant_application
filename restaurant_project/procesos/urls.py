from django.conf.urls import url
from procesos import views

app_name = 'procesos'

urlpatterns = [
    url('^usuarios/', views.registro_usuario, name='registro_usuarios'),
]