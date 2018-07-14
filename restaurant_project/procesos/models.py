from django.db import models
import restaurant_application as restaurant
from django.contrib.auth.models import User

class PerfilDeUsuario(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil')
    empleado = models.OneToOneField(restaurant.models.Empleado)
    foto_de_perfil = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.usuario.username
    
class Sesion(models.Model):
    caja = models.ForeignKey(restaurant.models.Caja)
    cajero = models.ForeignKey(restaurant.models.Empleado)
    fecha_apertura = models.DateTimeField(auto_now=True)
    fecha_cierre = models.DateTimeField(blank = True)
    monto_apertura = models.FloatField()
    monto_real = models.FloatField()
    estado = models.CharField(max_length=20)

    def calcularMontoEstimado(self):
        pass

    def calcularDiferencia(self):
        pass
    
class Orden(models.Model):
    sesion = models.ForeignKey(Sesion, related_name="orden")
    mesero = models.ForeignKey(restaurant.models.Empleado)
    cliente = models.ForeignKey(restaurant.models.Caja, blank=True)
    mesa = models.ForeignKey(restaurant.models.Mesa)

    fecha_orden = models.DateTimeField(auto_now=True)
    descuento = models.FloatField(blank=True)
    propina = models.FloatField(default=0.10)
    estado = models.CharField(max_length=20)
    comentario = models.TextField(max_length=512)

    def calcularTotal(self):
        pass

    
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name="detalles_de_orden")
    consumible = models.ForeignKey(restaurant.models.Platillo)
    cantidad = models.PositiveIntegerField()
    precio_de_venta = models.FloatField()
    comentario = models.CharField(max_length=128)

    def calcularSubtotal(self):
        pass
