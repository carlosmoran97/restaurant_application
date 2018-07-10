from django import forms
from .models import CategoriaPlatillo

class CategoriaPlatilloForm(forms.ModelForm):

    class Meta:
        model = CategoriaPlatillo
        fields = [
            'categoria'
        ]

        widgets = {
            'categoria':forms.TextInput(attrs={'class':'form-control','id':'txtCategoria'}),
        }
