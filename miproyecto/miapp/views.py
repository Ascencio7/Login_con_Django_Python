from django.shortcuts import render

# nueva importacion
from django.http import HttpResponse

# Create your views here.

# Funcion para probar si funciona xd
def inicio(request):
    return HttpResponse("Bienvenidos a la apliacion de Vladi :D")