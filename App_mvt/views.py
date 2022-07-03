from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from App_mvt.models import Familia
# Create your views here.

def listar_familia (request):
    context = {}
    context ["familiares"] = Familia.objects.all() 
    return render (request, "App_mvt/index.html", context)
