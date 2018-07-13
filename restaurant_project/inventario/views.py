from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from inventario.models import Producto, ReporteDeExistencia, Existencia
from inventario.serializers import ProductoSerializer, ExistenciaSerializer
from django.http import JsonResponse
from inventario.forms import ProductoForm, ExistenciaForm
from django.views.generic import ListView, DetailView

class Get_producto_Create(APIView):
    def get(self, request):
        producto = Producto.objects.create(nombre=request.GET['nombre'], unidad_de_medida=request.GET['unidad_de_medida'])
        producto.save()
        return JsonResponse({'respuesta':'ok'})

class Get_producto_Update(APIView):
    def get(self, request):
        producto = Producto.objects.filter(id=request.GET['id']).update(nombre=request.GET['nombre'], unidad_de_medida=request.GET['unidad_de_medida'])
        return JsonResponse({'respuesta':'ok'})


class Get_producto_Delete(APIView):
    def get(self, request):
        producto = Producto.objects.filter(id=request.GET['id']).delete()
        return JsonResponse({'respuesta':'ok'})

class Get_producto_List(APIView):
    def get(self, request):
        productos = Producto.objects.all().order_by("id")
        serialized = ProductoSerializer(productos, many=True)
        return Response(serialized.data)

class Get_producto_ListFilter(APIView):
    def get(self, request):
        productos = Producto.objects.filter(nombre__startswith=request.GET['nombre']).order_by('id')
        serialized = ProductoSerializer(productos, many=True)
        return Response(serialized.data)

def productos(request):
    form = ProductoForm()
    context = {'form':form}
    return render(request, 'inventario/productos.html', context)

class ReporteDeExistenciaList(ListView):
    model = ReporteDeExistencia
    context_object_name = 'reportes'

class ReporteDeExistenciaDetail(DetailView):
    model = ReporteDeExistencia
    context_object_name = 'reporte'
    template_name = 'inventario/reportedeexistencia_detail.html'
    existenciaForm = ExistenciaForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.existenciaForm
        return context

class GetExistenciasList(APIView):
    def get(self, request):
        existencias = Existencia.objects.filter(reporte_de_existencia=request.GET['id_reporte']).order_by('id')
        serialized = ExistenciaSerializer(existencias, many=True)
        return Response(serialized.data)

class GetExistenciasCreate(APIView):
    def get(self, request):
        id_producto = int(request.GET['id_producto'])
        producto = Producto.objects.filter(id=id_producto).get()
        id_reporte = int(request.GET['id_reporte'])
        reporte = ReporteDeExistencia.objects.filter(id=id_reporte).get()
        existencia = Existencia.objects.create(reporte_de_existencia=reporte, producto=producto ,existencias=request.GET['existencias'])
        existencia.save()
        return JsonResponse({'respuesta':'ok'})