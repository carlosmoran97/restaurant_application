from django.contrib import admin
from inventario.models import Producto, Existencia, ReporteDeExistencia


# modelos de la aplicación de inventario

admin.site.register(Producto)
admin.site.register(Existencia)
admin.site.register(ReporteDeExistencia)
