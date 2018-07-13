from django import forms
from inventario.models import Producto, Existencia

class ProductoForm(forms.ModelForm):

    class Meta():
        model = Producto
        fields = ('nombre', 'unidad_de_medida',)

class ExistenciaForm(forms.ModelForm):

    class Meta():
        model = Existencia
        fields = ('producto', 'existencias')