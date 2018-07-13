from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriaPlatillo, Platillo, Mesa, Empleado, Puesto, Asignacion
from .serializers import CategoriaPlatilloSerializer, PlatilloSerializer, MesaSerializer
from .forms import CategoriaPlatilloForm, PlatilloForm, MesaForm, EmpleadoForm, PuestoForm, AsignacionForm
from django.http import JsonResponse

"""
    VIEWS PARA CATEGORIA PLATILLO
"""

def index_categoria_platillos(request):
    form = CategoriaPlatilloForm()
    context = {'form':form}
    return render(request, 'restaurant_application/categoria_platillos/index.html', context)

class CategoriaPlatilloCreate(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.create(categoria=request.POST['categoria'])
        categoriaplatillo.save()
        return JsonResponse({'respuesta':'correctamente!'})

class CategoriaPlatilloUpdate(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.POST['idCategoriaPlatillo']).update(categoria=request.POST['categoria'])
        return JsonResponse({'respuesta':'correctamente!'})

class CategoriaPlatilloDelete(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.POST['idCategoriaPlatillo']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class CategoriaPlatilloList(APIView):
    def post(self, request):
        categoriaplatillos = CategoriaPlatillo.objects.all().order_by("-idCategoriaPlatillo")
        serialized = CategoriaPlatilloSerializer(categoriaplatillos, many=True)
        return Response(serialized.data)

class CategoriaPlatilloListFilter(APIView):
    def post(self, request):
        categoriaplatillos = CategoriaPlatillo.objects.filter(categoria__startswith=request.POST['categoria']).order_by("-idCategoriaPlatillo")
        serialized = CategoriaPlatilloSerializer(categoriaplatillos, many=True)
        return Response(serialized.data)

"""
    VIEWS PARA PLATILLOS
"""

def index_platillos(request):
    form = PlatilloForm()
    context = {'form':form}
    return render(request, 'restaurant_application/platillos/index.html', context)

class PlatilloCreate(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.POST['categoria_platillo'])
        platillo = Platillo.objects.create(nombre=request.POST['nombre'], precioUnitario=request.POST['precioUnitario'], categoria_platillo=categoriaplatillo[0])
        platillo.save()
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloUpdate(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.POST['categoria_platillo'])
        platillo = Platillo.objects.filter(codigoPlatillo=request.POST['codigoPlatillo']).update(nombre=request.POST['nombre'], precioUnitario=request.POST['precioUnitario'], categoria_platillo=categoriaplatillo[0])
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloDelete(APIView):
    def post(self, request):
        platillo = Platillo.objects.filter(codigoPlatillo=request.POST['codigoPlatillo']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloList(APIView):
    def post(self, request):
        platillos = Platillo.objects.all().order_by("-codigoPlatillo")
        serialized = PlatilloSerializer(platillos, many=True)
        return Response(serialized.data)

"""
    VIEWS PARA MESAS
"""

def index_mesas(request):
    form = MesaForm()
    context = {'form':form}
    return render(request, 'restaurant_application/mesas/index.html', context)

class MesaCreate(APIView):
    def post(self, request):
        mesa = Mesa.objects.create(numero_mesa=request.POST['numero_mesa'], asientos=request.POST['asientos'])
        mesa.save()
        return JsonResponse({'respuesta':'correctamente!'})

class MesaUpdate(APIView):
    def post(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.POST['codigo_mesa']).update(numero_mesa=request.POST['numero_mesa'], asientos=request.POST['asientos'])
        return JsonResponse({'respuesta':'correctamente!'})

class MesaDelete(APIView):
    def post(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.POST['codigo_mesa']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class MesaList(APIView):
    def post(self, request):
        mesas = Mesa.objects.all().order_by("-codigo_mesa")
        serialized = MesaSerializer(mesas, many=True)
        return Response(serialized.data)

"""
    VIEWS PARA EMPLEADOS
"""

def index_empleados(request):
    formEmpleado = EmpleadoForm()
    formPuesto = PuestoForm()
    formAsignacion = AsignacionForm()
    context = {'formEmpleado':formEmpleado,'formAsignacion':formAsignacion}
    return render(request, 'restaurant_application/empleados/index.html', context)


class EmpleadoCreate(APIView):
    def post(self, request):
        empleado = Empleado.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], fecha_nacimiento=request.POST['fecha_nacimiento'], dui=request.POST['dui'], nit=request.POST['nit'], afp=request.POST['afp'])
        puesto = Puesto.objects.filter(idPuesto=request.POST['idPuesto'])
        asignacion = Asignacion.objects.create(empleado=empleado, puesto=puesto[0], salario=request.POST['salario'], fecha_contratacion=request.POST['fecha_contratacion'])
        return JsonResponse({'respuesta':'correctamente!'})
"""

class MesaUpdate(APIView):
    def post(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.POST['codigo_mesa']).update(numero_mesa=request.POST['numero_mesa'], asientos=request.POST['asientos'])
        return JsonResponse({'respuesta':'correctamente!'})

class MesaDelete(APIView):
    def post(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.POST['codigo_mesa']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class MesaList(APIView):
    def post(self, request):
        mesas = Mesa.objects.all().order_by("-codigo_mesa")
        serialized = MesaSerializer(mesas, many=True)
        return Response(serialized.data)
"""
