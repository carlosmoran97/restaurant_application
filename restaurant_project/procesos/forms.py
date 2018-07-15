from django import forms
from django.contrib.auth.models import User
from procesos.models import PerfilDeUsuario, Sesion
from restaurant_application.models import Asignacion, Empleado, Puesto

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password')

class PerfilDeUsuarioForm(forms.ModelForm):
    class Meta():
        model = PerfilDeUsuario
        fields = ('empleado', 'foto_de_perfil')

class SesionForm(forms.ModelForm):
    class Meta():
        model = Sesion
        fields = ('caja', 'cajero', 'fecha_cierre', 'monto_apertura', 'monto_real', 'estado')
        widgets = {
            'caja':forms.Select(attrs={'class':'form-control','id':'selectCaja'}),
            'cajero':forms.Select(attrs={'class':'form-control','id':'selectCajero'}),
            'monto_apertura':forms.TextInput(attrs={'class':'form-control','id':'txtMontoApertura'}),
            'monto_real':forms.TextInput(attrs={'class':'form-control','id':'txtMontoReal'}),
        }
