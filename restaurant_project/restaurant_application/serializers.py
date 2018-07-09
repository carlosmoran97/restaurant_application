from rest_framework import serializers
from .models import CategoriaPlatillo

class CategoriaPlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPlatillo
        fields = '__all__'
