from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("¡Trabajando desde Render!")
# Create your views here.
