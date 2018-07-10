from django import forms
from .models import CategoriaPlatillo, Platillo

class CategoriaPlatilloForm(forms.ModelForm):

    class Meta:
        model = CategoriaPlatillo
        fields = [
            'categoria'
        ]

        widgets = {
            'categoria':forms.TextInput(attrs={'class':'form-control','id':'txtCategoria'}),
        }

class PlatilloForm(forms.ModelForm):

    class Meta:
        model = Platillo
        fields = [
            'nombre',
            'precioUnitario',
            'idCategoriaPlatillo'
        ]

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'txtNombre'}),
            'precioUnitario':forms.TextInput(attrs={'class':'form-control','id':'txtPrecioUnitario'}),
            'idCategoriaPlatillo':forms.Select(attrs={'class':'form-control','id':'selectidCategoriaPlatillo'})
        }
