from rest_framework import serializers
from inventario.models import Producto, Existencia

class ProductoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Producto
        fields = '__all__'

class ExistenciaSerializer(serializers.ModelSerializer):

    producto = ProductoSerializer(many=False, read_only=True)

    class Meta():
        model = Existencia
        fields = '__all__'