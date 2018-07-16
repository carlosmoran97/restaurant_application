from rest_framework import serializers
from .models import Sesion, Orden
from restaurant_application.serializers import CajaSerializer, EmpleadoSerializer, MesaSerializer

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
        fields = ('sesion', 'mesero', 'cliente', 'mesa', 'fecha_orden', 'descuento', 'propina', 'estado', 'comentario')
