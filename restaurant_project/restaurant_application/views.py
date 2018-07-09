from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

def index_categoria_platillos(request):
    return render(request, 'restaurant_application/categoria_platillos/index.html')
