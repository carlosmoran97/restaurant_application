from rest_framework import serializers
from .models import CategoriaPlatillo, Platillo, Mesa, Empleado, Puesto, Asignacion, Caja, Cliente

class CategoriaPlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPlatillo
        fields = '__all__'

class PlatilloSerializer(serializers.ModelSerializer):
    categoria_platillo = CategoriaPlatilloSerializer(many=False)
    class Meta:
        model = Platillo
        fields = ('codigoPlatillo', 'nombre', 'precioUnitario', 'categoria_platillo')

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ('codigo_mesa', 'numero_mesa', 'asientos', 'ocupado')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('idEmpleado', 'nombre', 'apellido', 'fecha_nacimiento', 'dui', 'nit', 'afp')

class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = ('idPuesto', 'puesto')

class AsignacionSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer(many=False)
    puesto = PuestoSerializer(many=False)
    class Meta:
        model = Asignacion
        fields = ('id', 'empleado', 'puesto', 'salario', 'fecha_contratacion')

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'

class CategoriaPlatilloConPlatillosSerializer(serializers.ModelSerializer):

    platillos = PlatilloSerializer(many=True, read_only=True)

    class Meta:
        model = CategoriaPlatillo
        fields = ('idCategoriaPlatillo', 'categoria', 'platillos')