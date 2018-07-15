from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from procesos.forms import PerfilDeUsuarioForm, UsuarioForm, SesionForm, OrdenForm
from procesos.serializers import SesionSerializer
from procesos.models import Sesion, Orden
from restaurant_application.models import Asignacion, Empleado, Puesto, Caja, Cliente, Mesa
from django.http import JsonResponse
import datetime
from django.views.generic import ListView, CreateView
# Create your views here.

def registro_usuario(request):
    registered = False

    if request.method == 'POST':
        user_form = UsuarioForm(data=request.POST)
        profile_form = PerfilDeUsuarioForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.usuario = user

            if 'foto_de_perfil' in request.FILES:
                profile.foto_de_perfil = request.FILES['foto_de_perfil']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UsuarioForm()
        profile_form = PerfilDeUsuarioForm()

    context_dict = {
        "registered": registered,
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'procesos/registro_usuario.html', context=context_dict)

def sesion_caja(request):
    form = SesionForm()
    context = {'form':form}
    return render(request, 'procesos/sesion_caja/index.html', context)

class CreateSesionCaja(APIView):
    def get(self, request):
        caja = Caja.objects.filter(id=request.GET['numero_caja']).get()
        cajero = Empleado.objects.filter(idEmpleado=request.GET['idEmpleado']).get()
        sesion = Sesion.objects.create(caja = caja, cajero=cajero, monto_apertura=request.GET['monto_apertura'], estado="Abierta")
        return JsonResponse({'respuesta':'correctamente!'})

class CerrarSesionCaja(APIView):
    def get(self, request):
        fecha_cierre = datetime.datetime.now()
        #fecha_cierr = fecha_cierre.year+"-"fecha_cierre.month+"-"+fecha_cierre.day+" "+fecha_cierre.hour+":"fecha_cierre.minute+":"fecha_cierre.second
        sesion = Sesion.objects.filter(id=request.GET['id']).update(monto_real=request.GET['monto_real'], fecha_cierre=fecha_cierre, estado="Cerrada")
        return JsonResponse({'respuesta':'correctamente!'})

class SesionList(APIView):
    def get(self, request):
        sesiones = Sesion.objects.all().order_by("-id")
        serialized = SesionSerializer(sesiones, many=True)
        return Response(serialized.data)

class DetalleSesionCaja(APIView):
    def get(self, request):
        sesiones = Sesion.objects.filter(id=request.GET['id'])
        serialized = SesionSerializer(sesiones, many=True)
        return Response(serialized.data)

class PanelMesasView(ListView):
    def get(self, request):
        formOrden = OrdenForm()
        context = {'formOrden':formOrden}
        return render(request, 'procesos/mesas.html', context)

class PanelMesasView(CreateView):
    model = Orden
    template_name = 'procesos/mesas.html'
    fields = ('mesero', 'comentario')
