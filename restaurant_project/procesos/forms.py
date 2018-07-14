from django import forms
from django.contrib.auth.models import User
from procesos.models import PerfilDeUsuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password')

class PerfilDeUsuarioForm(forms.ModelForm):
    class Meta():
        model = PerfilDeUsuario
        fields = ('empleado', 'foto_de_perfil')