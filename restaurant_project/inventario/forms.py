from django import forms
from inventario.models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'unidad_de_medida',)