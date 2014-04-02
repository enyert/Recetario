from RecetarioApp.models import *
from django.http import HttpResponse, Http404
from django.core import serializers
from django.contrib.auth.models import User
import operator
from django.db.models import Q

def serializar(lista):
    return serializers.serialize("json", lista)

def buscarRecetasPorCategoria(request, clave):
    if request.method == 'GET':
        recetas = Receta.objects.filter(categoria__nombre__icontains = clave)
        data = serializar(recetas)
        return HttpResponse(data, mimetype='application/json')
    else:
        return Http404

def buscarRecetasPorIngredientes(request, lista_ingredientes):
    claves = str(lista_ingredientes).split(',')

    if request.method == 'GET':
        recetas = Receta.objects.filter(ingredientes__nombre__icontains = claves[0])
        for i in range(1,len(claves)):
            recetas = recetas.filter(ingredientes__nombre__icontains = claves[i])
    else:
        return Http404

