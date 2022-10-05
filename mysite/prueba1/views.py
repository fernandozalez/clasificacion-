from django.shortcuts import render
from .models import post

def muestra_datos(request):
    consulta = post.objects.all()
    lissum = suma (consulta)
    contexto = zip(consulta, lissum)
    return render(request, 'prueba1/index.html',{'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum
