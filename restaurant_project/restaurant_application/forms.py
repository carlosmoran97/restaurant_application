from django import forms
from .models import CategoriaPlatillo, Platillo, Mesa, Empleado, Puesto, Asignacion
import time

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

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'dui',
            'nit',
            'afp'
        ]

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','id':'txtNombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control','id':'txtApellido'}),
            'fecha_nacimiento': forms.SelectDateWidget(years=range(1950, int(time.strftime("%Y"))+1),attrs={'class':'form-control'}),
            'dui':forms.TextInput(attrs={'class':'form-control','id':'txtDUI'}),
            'nit':forms.TextInput(attrs={'class':'form-control','id':'txtNIT'}),
            'afp':forms.TextInput(attrs={'class':'form-control','id':'txtAFṔ'}),
        }

class PuestoForm(forms.ModelForm):

    class Meta:
        model = Puesto
        fields = [
            'puesto',
        ]

        widgets = {
            'puesto':forms.Select(attrs={'class':'form-control','id':'selectPuesto'})
        }

class AsignacionForm(forms.ModelForm):

    class Meta:
        model = Asignacion
        fields = [
            'puesto',
            'salario',
            'fecha_contratacion'
        ]

        widgets = {
            'puesto':forms.Select(attrs={'class':'form-control','id':'selectPuesto'}),
            'salario':forms.TextInput(attrs={'class':'form-control','id':'txtSalario'}),
            'fecha_contratacion': forms.SelectDateWidget(years=range(1950, int(time.strftime("%Y"))+1),attrs={'class':'form-control'})
        }
