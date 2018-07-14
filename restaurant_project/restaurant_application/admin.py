from django.contrib import admin
from restaurant_application.models import (Asignacion, CategoriaPlatillo, 
Empleado, Mesa, Platillo, Puesto, Caja, Cliente)

# modelos de la aplicación de restaurante

admin.site.register(Asignacion)
admin.site.register(CategoriaPlatillo)
admin.site.register(Empleado)
admin.site.register(Mesa)
admin.site.register(Platillo)
admin.site.register(Puesto)
admin.site.register(Caja)
admin.site.register(Cliente)