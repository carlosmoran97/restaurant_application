from rest_framework import serializers
from .models import Sesion, Orden, DetalleOrden
from restaurant_application.serializers import CajaSerializer, EmpleadoSerializer, MesaSerializer, PlatilloSerializer

class SesionSerializer(serializers.ModelSerializer):
    caja = CajaSerializer(many=False)
    cajero = EmpleadoSerializer(many=False)

    class Meta:
        model = Sesion
        fields = ('id', 'caja', 'cajero', 'fecha_apertura', 'fecha_cierre', 'monto_apertura', 'monto_real', 'estado')

class OrdenSerializer(serializers.ModelSerializer):
    sesion = SesionSerializer(many=False)
    mesero = EmpleadoSerializer(many=False)
    mesa = MesaSerializer(many=False)
    class Meta:
        model = Orden
        fields = ('id','sesion', 'mesero', 'cliente', 'mesa', 'fecha_orden', 'propina', 'estado', 'comentario')

class DetalleOrdenSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer(many=False)
    consumible = PlatilloSerializer(many=False)
    class Meta:
        model = DetalleOrden
        fields = '__all__'

class Orden_ConDetalle_Serializer(serializers.ModelSerializer):
    detalles_de_orden = DetalleOrdenSerializer(many = True)
    class Meta:
        model = Orden
        fields = fields = ('id','sesion', 'mesero', 'cliente', 'mesa', 'fecha_orden', 'propina', 'estado', 'comentario', 'detalles_de_orden')