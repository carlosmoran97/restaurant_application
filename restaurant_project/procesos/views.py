from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from procesos.forms import PerfilDeUsuarioForm, UsuarioForm, SesionForm, OrdenForm
from procesos.serializers import SesionSerializer, OrdenSerializer, DetalleOrdenSerializer, Orden_ConDetalle_Serializer
from procesos.models import Sesion, Orden, DetalleOrden, cantidad_ordenes_del_dia, Pago
from restaurant_application.models import Asignacion, Empleado, Puesto, Caja, Cliente, Mesa, Platillo
from django.http import JsonResponse
import datetime
from django.views.generic import ListView, CreateView, DetailView
from django.views import View
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
# use estos para el login

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# Vistas
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
        formOrdenar = OrdenForm()
        context = {'formOrdenar':formOrdenar}
        return render(request, 'procesos/mesas.html', context)

class AbrirOrden(APIView):
    def get(self, request):
        sesion = Sesion.objects.filter(id=1)
        empleado = Empleado.objects.filter(idEmpleado=request.GET['idEmpleado'])
        mesa = Mesa.objects.filter(codigo_mesa=request.GET['codigo_mesa'])
        mesa.update(ocupado=True)
        orden = Orden.objects.create(sesion=sesion[0],numero_orden=cantidad_ordenes_del_dia() + 1, mesero=empleado[0], cliente=request.GET['cliente'], mesa=mesa[0], comentario=request.GET['comentario'])
        return JsonResponse({'respuesta':orden.id})

class detalle_orden(DetailView):
    model = Orden
    template_name = 'procesos/detalle_orden.html'

class OrdenDetail(APIView):
    def get(self, request):
        orden = Orden.objects.filter(id=request.GET['id'])
        serialized = OrdenSerializer(orden, many=True)
        return Response(serialized.data)

class OrdenDetailMesa(APIView):
    def get(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.GET['codigo_mesa'])
        orden = Orden.objects.filter(mesa=mesa[0], estado="No Finalizado")
        serialized = OrdenSerializer(orden, many=True)
        return Response(serialized.data)

class OrdenConDetallesDetailList(APIView):
    def get(self, request):
        ordenes = Orden.objects.filter(estado=request.GET['estado'])
        serialized = Orden_ConDetalle_Serializer(ordenes, many=True)
        return Response(serialized.data)

class OrdenPago(APIView):
    def get(self, request):
        orden = Orden.objects.filter(id=request.GET['id']).get()
        serialized = Orden_ConDetalle_Serializer(orden, many=False)
        return Response(serialized.data)

class GetOrdenesList(APIView):
    def get(self, request):
        ordenes = Orden.objects.all()
        serialized = OrdenSerializer(ordenes, many=True)
        return Response(serialized.data)

class GetOrdenesPorEstadoList(APIView):
    def get(self, request):
        ordenes = Orden.objects.filter(estado=request.GET["estado"])
        serialized = OrdenSerializer(ordenes, many=True)
        return Response(serialized.data)

class GetOrdenesUpdate(APIView):
    def get(self, request):
        id = request.GET["id"]
        estado = request.GET["estado"]
        orden = Orden.objects.filter(id=id)
        orden.update(estado=estado)
        mesa = Mesa.objects.filter(codigo_mesa=orden[0].mesa.codigo_mesa)
        mesa.update(ocupado=False)

        return Response({"respuesto": "ok"})

class FacturarView(View):
    def get(self, request):
        return render(request, 'procesos/facturar.html')

class OrdenesActivas(View):
    def get(self, request):
        return render(request, 'procesos/ordenes_activas.html')

class CreateDetalleOrden(APIView):
    def get(self, request):
        orden = Orden.objects.filter(id=request.GET['id'])
        consumible = Platillo.objects.filter(codigoPlatillo=request.GET['codigoPlatillo'])
        detalleorden = DetalleOrden.objects.create(orden=orden[0], consumible=consumible[0], cantidad=1, precio_de_venta=request.GET['precio'], comentario='', descuento=0)
        return JsonResponse({'id':detalleorden.id})

class UpdateDetalleOrden(APIView):
    def get(self, request):
        detalleorden = DetalleOrden.objects.filter(id=request.GET['id']).update(cantidad=request.GET['cantidad'], precio_de_venta=request.GET['precio'], comentario='', descuento=request.GET['descuento'])
        return JsonResponse({'respuesta':' correctamente!'})

class DeleteDetalleOrden(APIView):
    def get(self, request):
        detalleorden = DetalleOrden.objects.filter(id=request.GET['id']).delete()
        return JsonResponse({'respuesta':' correctamente!'})

class DetalleOrdenDetail(APIView):
    def get(self, request):
        orden = Orden.objects.filter(id=request.GET['id'])
        detalleordenes = DetalleOrden.objects.filter(orden=orden[0])
        serialized = DetalleOrdenSerializer(detalleordenes, many=True)
        return Response(serialized.data)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Cuenta no activada')
        else:
            print("Alguien intentó ingresar y no pudo.")
            print("Usuario: {} y contraseña: {}".format(username, password))
            return HttpResponse("Proprocionó datos de ingreso erróneos.")
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def index(request):
    return render(request, 'index.html')

class PagoView(View):
    def get(self, request, pk):
        return render(request, "procesos/pago.html", {"pk":pk})


class Pagar(APIView):
    def get(self, request):
        entregado = request.GET['entregado']
        orden = Orden.objects.filter(id=request.GET['id'])

        pago = Pago.objects.create(orden=orden, entregado=entregado)
        return JsonResponse({"respuesta":"ok"})


class FacturaView(View):
    def get(self, request, pk):
        orden = Orden.objects.get(id=pk)

        orden_serialized = Orden_ConDetalle_Serializer(orden, many=False)

        datos = orden_serialized.data

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(pk)

        buffer = BytesIO()

        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        p.rotate(90)
        p.setFont("Helvetica", 9)

        # generando el pdf

        p.drawString(height - 2.5 * cm, -(8.15 + (0.6 * 15)) * cm, "${:.2f}".format(datos['total']))
        p.drawString(height - 2.5 * cm, -(8.15 + (0.6 * 20)) * cm, "${:.2f}".format(datos['total']))
        p.drawString(height - 2.5 * cm, -(8.15 + (0.6 * 14)) * cm, "${:.2f}".format(datos['total'] / (1+datos["propina"])*datos["propina"]))
        p.drawString(height - 13.3 * cm, -(8.15 + (0.6 * 14)) * cm, "{}%".format(int(datos["propina"]*100)))
        p.drawString(height - 12.2 * cm, -(8.15 + (0.6 * 14)) * cm, "Propina")
        i = 0

        for detalle in datos['detalles_de_orden']:
            p.drawString(height - 13.2 * cm, -(8.15+(0.6*i)) * cm, str(detalle["cantidad"]))
            p.drawString(height - 12.2 * cm, -(8.15+(0.6*i)) * cm, detalle["consumible"]["nombre"])
            precio_unitario = "${:.2f}".format(detalle["precio_de_venta"]*(1-detalle["descuento"]/100))
            p.drawString(height - 6 * cm, -(8.15+(0.6*i)) * cm, precio_unitario)
            subtotal = "${:.2f}".format(detalle["subtotal"])
            p.drawString(height - 2.5 * cm, -(8.15+(0.6*i)) * cm, subtotal)
            i = i + 1

        # finalizado
        p.showPage()
        p.save()

        response.write(buffer.getvalue())
        buffer.close()

        return response


class GetCreatePago(APIView):
    def get(self, request):
        id = request.GET['id']
        entregado = request.GET['entregado']

        orden = Orden.objects.filter(id=id).get()

        pago = Pago.objects.create(orden=orden, entregado=entregado)

        return JsonResponse({"respuesta":"ok"})