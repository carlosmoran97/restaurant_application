from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriaPlatillo, Platillo
from .serializers import CategoriaPlatilloSerializer, PlatilloSerializer
from .forms import CategoriaPlatilloForm
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
    return render(request, 'restaurant_application/platillos/index.html')

class PlatilloCreate(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.POST['idCategoriaPlatillo'])
        platillo = Platillo.objects.create(nombre=request.POST['nombre'], precioUnitario=request.POST['precioUnitario'], idCategoriaPlatillo=categoriaplatillo)
        platillo.save()
        return JsonResponse({'respuesta':'correctamente!'})

class PlatilloUpdate(APIView):
    def post(self, request):
        categoriaplatillo = CategoriaPlatillo.objects.filter(idCategoriaPlatillo=request.POST['idCategoriaPlatillo'])
        platillo = Platillo.objects.filter(codigoPlatillo=request.POST['codigoPlatillo']).update(nombre=request.POST['nombre'], precioUnitario=request.POST['precioUnitario'], idCategoriaPlatillo=categoriaplatillo)
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
