from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoriaPlatillo
from .serializers import CategoriaPlatilloSerializer
from django.http import JsonResponse

def index_categoria_platillos(request):
    return render(request, 'restaurant_application/categoria_platillos/index.html')

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
    def get(self, request):
        categoriaplatillos = CategoriaPlatillo.objects.all().order_by("-idCategoriaPlatillo")
        serialized = CategoriaPlatilloSerializer(categoriaplatillos, many=True)
        return Response(serialized.data)
