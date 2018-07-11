from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from inventario.models import Producto
from inventario.serializers import ProductoSerializer
from django.http import JsonResponse
from inventario.forms import ProductoForm

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