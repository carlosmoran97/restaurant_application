from django.contrib import admin
from inventario.models import Producto, Existencia, ReporteDeExistencia
from restaurant_application.models import Asignacion, CategoriaPlatillo, Empleado, Mesa, Platillo, Puesto

# modelos de la aplicación de inventario

admin.site.register(Producto)
admin.site.register(Existencia)
admin.site.register(ReporteDeExistencia)

# modelos de la aplicación de restaurante

admin.site.register(Asignacion)
admin.site.register(CategoriaPlatillo)
admin.site.register(Empleado)
admin.site.register(Mesa)
admin.site.register(Platillo)
admin.site.register(Puesto)