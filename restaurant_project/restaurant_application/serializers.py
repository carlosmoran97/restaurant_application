from rest_framework import serializers
from .models import CategoriaPlatillo, Platillo

class CategoriaPlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPlatillo
        fields = '__all__'


class PlatilloSerializer(serializers.ModelSerializer):
    categoria_platillo = CategoriaPlatilloSerializer(many=False)
    class Meta:
        model = Platillo
        fields = ('codigoPlatillo', 'nombre', 'precioUnitario', 'categoria_platillo')
