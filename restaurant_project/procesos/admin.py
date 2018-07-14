from django.contrib import admin
from procesos.models import PerfilDeUsuario, DetalleOrden, Orden, Sesion

admin.site.register(PerfilDeUsuario)
admin.site.register(DetalleOrden)
admin.site.register(Orden)
admin.site.register(Sesion)