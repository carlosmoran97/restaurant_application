from django import forms
from .models import CategoriaPlatillo, Platillo, Mesa

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
            'categoria_platillo'
        ]

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'txtNombre'}),
            'precioUnitario':forms.TextInput(attrs={'class':'form-control','id':'txtPrecioUnitario'}),
            'categoria_platillo':forms.Select(attrs={'class':'form-control','id':'selectCategoriaPlatillo'})
        }

class MesaForm(forms.ModelForm):

    class Meta:
        model = Mesa
        fields = [
            'numero_mesa',
            'asientos',
            'ocupado'
        ]

        widgets = {
            'numero_mesa':forms.TextInput(attrs={'class':'form-control','id':'txtNumeroMesa'}),
            'asientos':forms.TextInput(attrs={'class':'form-control','id':'txtAsientos'}),
            'ocupado':forms.Select(attrs={'class':'form-control','id':'selectEstado'})
        }
