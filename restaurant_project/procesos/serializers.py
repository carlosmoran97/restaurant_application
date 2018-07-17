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
<<<<<<< HEAD

class DetalleOrdenSerializer(serializers.ModelSerializer):
    orden = OrdenSerializer(many=False)
    consumible = PlatilloSerializer(many=False)
    class Meta:
        model = DetalleOrden
        fields = '__all__'
=======
>>>>>>> 50155b191a52ed5528ba46edb09bca50346985d3
