from rest_framework import serializers
from .models import Sesion
from restaurant_application.serializers import CajaSerializer, ClienteSerializer, EmpleadoSerializer

class SesionSerializer(serializers.ModelSerializer):
    caja = CajaSerializer(many=False)
    cajero = EmpleadoSerializer(many=False)

    class Meta:
        model = Sesion
        fields = ('id', 'caja', 'cajero', 'fecha_apertura', 'fecha_cierre', 'monto_apertura', 'monto_real', 'estado')
