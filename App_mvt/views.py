from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

# Create your views here.

def mostrar_plantilla (request):
    return render (request, "App_mvt/index.html")