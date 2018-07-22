from django.db import models
import restaurant_application as restaurant
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator


class PerfilDeUsuario(models.Model):
    usuario = models.OneToOneField(User, related_name='perfil')
    empleado = models.OneToOneField(restaurant.models.Empleado)
    foto_de_perfil = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.usuario.username


class Sesion(models.Model):
    caja = models.ForeignKey(restaurant.models.Caja)
    cajero = models.ForeignKey(restaurant.models.Empleado)
    fecha_apertura = models.DateTimeField(auto_now=True)
    fecha_cierre = models.DateTimeField(null=True)
    monto_apertura = models.DecimalField(max_digits=20, decimal_places=2)
    monto_real = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    estado = models.CharField(max_length=20)

    def calcularMontoEstimado(self):
        pass

    def calcularDiferencia(self):
        pass


class Orden(models.Model):
    sesion = models.ForeignKey(Sesion, related_name="orden")
    numero_orden = models.PositiveIntegerField(default=0)
    mesero = models.ForeignKey(restaurant.models.Empleado)
    cliente = models.CharField(max_length=500, null=True)
    mesa = models.ForeignKey(restaurant.models.Mesa)
    fecha_orden = models.DateTimeField(auto_now=True)
    propina = models.FloatField(default=0.10)
    estado = models.CharField(max_length=20, default="No Finalizado")
    comentario = models.TextField(max_length=512)

    @property
    def total(self):
        total = 0
        detalles = DetalleOrden.objects.filter(orden=self.id)
        for detalle in detalles:
            total = total + detalle.subtotal
        total = total * (1 + self.propina)
        return total


def cantidad_ordenes_del_dia():
    numero = 0
    for orden in Orden.objects.all():
        if orden.fecha_orden.year == datetime.now().year and orden.fecha_orden.month == datetime.now().month and orden.fecha_orden.day == datetime.now().day:
            numero = numero + 1

    return numero


class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name="detalles_de_orden")
    consumible = models.ForeignKey(restaurant.models.Platillo)
    cantidad = models.PositiveIntegerField(default=1)
    ordenados = models.PositiveIntegerField(default=1)
    entregados = models.PositiveIntegerField(default=0)
    precio_de_venta = models.FloatField()
    comentario = models.CharField(max_length=128)
    descuento = models.FloatField(null=True, default=0)

    @property
    def subtotal(self):
        return (self.precio_de_venta * self.cantidad) * (1 - (self.descuento / 100))


class Pago(models.Model):
    orden = models.ForeignKey(Orden, related_name="pago")
    entregado = models.FloatField(validators=[MinValueValidator(0.0)])

    @property
    def cambio(self):
        orden = Orden.objects.filter(id=self.orden).get()
        return self.entregado - orden.total
