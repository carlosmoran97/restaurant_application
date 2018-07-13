from django.contrib import admin
from inventario.models import Producto, Existencia, ReporteDeExistencia
# Register your models here.

admin.site.register(Producto)
admin.site.register(Existencia)
admin.site.register(ReporteDeExistencia)