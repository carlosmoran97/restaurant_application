from rest_framework import serializers
from inventario.models import Producto, Existencia, ReporteDeExistencia

class ProductoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Producto
        fields = '__all__'

class ExistenciaSerializer(serializers.ModelSerializer):

    producto = ProductoSerializer(many=False, read_only=True)

    class Meta():
        model = Existencia
        fields = '__all__'

class ReporteDeExistenciaSerializer(serializers.ModelSerializer):

    existencias = ExistenciaSerializer(many=True, read_only=True)

    class Meta():
        model = ReporteDeExistencia
        fields = '__all__'