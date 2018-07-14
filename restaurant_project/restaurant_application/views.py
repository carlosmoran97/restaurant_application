from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriaPlatillo, Platillo, Mesa, Empleado, Puesto, Asignacion
from .serializers import CategoriaPlatilloSerializer, PlatilloSerializer, MesaSerializer, EmpleadoSerializer, PuestoSerializer, AsignacionSerializer
from .forms import CategoriaPlatilloForm, PlatilloForm, PlatilloFormSelect, MesaForm, EmpleadoForm, PuestoForm, AsignacionForm
from django.http import JsonResponse

"""
    VIEWS PARA CATEGORIA PLATILLO
"""

def index_categoria_platillos(request):
    form = CategoriaPlatilloForm()
    context = {'form':form}
    return render(request, 'restaurant_application/categoria_platillos/index.html', context)

class CategoriaPlatilloCreate(APIView):
    def get(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.create(categoria=request.GET['categoria'])
        categoriaplatillo.save()
        return JsonResponse({'respuesta':'correctamente!'})

class CategoriaPlatilloUpdate(APIView):
    def get(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.GET['idCategoriaPlatillo']).update(categoria=request.GET['categoria'])
        return JsonResponse({'respuesta':'correctamente!'})

class CategoriaPlatilloDelete(APIView):
    def get(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.GET['idCategoriaPlatillo']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class CategoriaPlatilloList(APIView):
    def get(self, request):
        categoriaplatillos = CategoriaPlatillo.objects.all().order_by("-idCategoriaPlatillo")
        serialized = CategoriaPlatilloSerializer(categoriaplatillos, many=True)
        return Response(serialized.data)

class CategoriaPlatilloListFilter(APIView):
    def get(self, request):
        categoriaplatillos = CategoriaPlatillo.objects.filter(categoria__startswith=request.GET['categoria']).order_by("-idCategoriaPlatillo")
        serialized = CategoriaPlatilloSerializer(categoriaplatillos, many=True)
        return Response(serialized.data)

"""
    VIEWS PARA PLATILLOS
"""

def index_platillos(request):
    form = PlatilloForm()
    form_e = PlatilloFormSelect()
    context = {'form':form, 'form_e':form_e}
    return render(request, 'restaurant_application/platillos/index.html', context)

class PlatilloCreate(APIView):
    def get(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.GET['categoria_platillo'])
        platillo = Platillo.objects.create(nombre=request.GET['nombre'], precioUnitario=request.GET['precioUnitario'], categoria_platillo=categoriaplatillo[0])
        platillo.save()
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloUpdate(APIView):
    def get(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.GET['categoria_platillo'])
        platillo = Platillo.objects.filter(codigoPlatillo=request.GET['codigoPlatillo']).update(nombre=request.GET['nombre'], precioUnitario=request.GET['precioUnitario'], categoria_platillo=categoriaplatillo[0])
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloDelete(APIView):
    def get(self, request):
        platillo = Platillo.objects.filter(codigoPlatillo=request.GET['codigoPlatillo']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloList(APIView):
    def get(self, request):
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
    def get(self, request):
        mesa = Mesa.objects.create(numero_mesa=request.GET['numero_mesa'], asientos=request.GET['asientos'])
        mesa.save()
        return JsonResponse({'respuesta':'correctamente!'})

class MesaUpdate(APIView):
    def get(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.GET['codigo_mesa']).update(numero_mesa=request.GET['numero_mesa'], asientos=request.GET['asientos'])
        return JsonResponse({'respuesta':'correctamente!'})

class MesaDelete(APIView):
    def get(self, request):
        mesa = Mesa.objects.filter(codigo_mesa=request.GET['codigo_mesa']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class MesaList(APIView):
    def get(self, request):
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
    def get(self, request):
        empleado = Empleado.objects.create(nombre=request.GET['nombre'], apellido=request.GET['apellido'], fecha_nacimiento=request.GET['fecha_nacimiento'], dui=request.GET['dui'], nit=request.GET['nit'], afp=request.GET['afp'])
        puesto = Puesto.objects.filter(idPuesto=request.GET['idPuesto'])
        asignacion = Asignacion.objects.create(empleado=empleado, puesto=puesto[0], salario=request.GET['salario'], fecha_contratacion=request.GET['fecha_contratacion'])
        return JsonResponse({'respuesta':'correctamente!'})


class EmpleadoUpdate(APIView):
    def get(self, request):
        empleado = Empleado.objects.filter(idEmpleado=request.GET['idEmpleado']).update(nombre=request.GET['nombre'], apellido=request.GET['apellido'], fecha_nacimiento=request.GET['fecha_nacimiento'], dui=request.GET['dui'], nit=request.GET['nit'], afp=request.GET['afp'])
        puesto = Puesto.objects.filter(idPuesto=request.GET['idPuesto'])
        asignacion = Asignacion.objects.filter(id=request.GET['id']).update(puesto=puesto[0], salario=request.GET['salario'], fecha_contratacion=request.GET['fecha_contratacion'])
        return JsonResponse({'respuesta':'correctamente!'})

class EmpleadoDelete(APIView):
    def get(self, request):
        empleado = Empleado.objects.filter(idEmpleado=request.GET['idEmpleado']).delete()
        asignacion = Asignacion.objects.filter(id=request.GET['id']).delete()
        return JsonResponse({'respuesta':'correctamente!'})

class EmpleadosList(APIView):
    def get(self, request):
        asignaciones = Asignacion.objects.all().order_by("-id")
        serialized = AsignacionSerializer(asignaciones, many=True)
        return Response(serialized.data)

class EmpleadoDetalle(APIView):
    def get(self, request):
        asignacion = Asignacion.objects.filter(id=request.GET['id'])
        serialized = AsignacionSerializer(asignacion, many=True)
        return Response(serialized.data)
