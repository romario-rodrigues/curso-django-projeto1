from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse # Nunca deixar de importar django.http HttpRequest e HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('HOME 1')

def sobre(request):
    return HttpResponse('Sobre 2')

def contato(request):
    return HttpResponse('Contato 3')

def historia(request):
    return HttpResponse('Historia 4')