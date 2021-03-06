from rest_framework import serializers
from .models import Sesion, Orden, DetalleOrden, PerfilDeUsuario
from restaurant_application.serializers import CajaSerializer, EmpleadoSerializer, MesaSerializer, PlatilloSerializer

class PerfilDeUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilDeUsuario
        fields = ('id','usuario', 'empleado')

class SesionSerializer(serializers.ModelSerializer):
    caja = CajaSerializer(many=False)
    cajero = EmpleadoSerializer(many=False)

    class Meta:
        model = Sesion
        fields = ('id', 'caja', 'cajero', 'fecha_apertura', 'fecha_cierre', 'monto_apertura', 'monto_estimado', 'monto_real', 'diferencia', 'estado')

class OrdenSerializer(serializers.ModelSerializer):
    sesion = SesionSerializer(many=False)
    mesero = EmpleadoSerializer(many=False)
    mesa = MesaSerializer(many=False)
    class Meta:
        model = Orden
        fields = ('id','numero_orden','sesion', 'mesero', 'cliente', 'mesa', 'fecha_orden', 'propina', 'estado', 'comentario')

class DetalleOrdenSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer(many=False)
    consumible = PlatilloSerializer(many=False)
    class Meta:
        model = DetalleOrden
        fields = ('id', 'orden', 'consumible', 'cantidad', 'ordenados', 'entregados', 'precio_de_venta', 'comentario', 'descuento', 'subtotal')


class Orden_ConDetalle_Serializer(serializers.ModelSerializer):
    detalles_de_orden = DetalleOrdenSerializer(many = True)
    sesion = SesionSerializer(many=False)
    mesero = EmpleadoSerializer(many=False)
    mesa = MesaSerializer(many=False)
    class Meta:
        model = Orden
        fields = ('id','numero_orden','sesion', 'mesero', 'cliente', 'mesa', 'fecha_orden', 'propina', 'estado', 'comentario', 'detalles_de_orden','total')
