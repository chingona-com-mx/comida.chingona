from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'nombre': 'Hola Mundo'
    }
    return render(request, 'home.html', context)


def home2(request):
    return HttpResponse('Hello, World!')
