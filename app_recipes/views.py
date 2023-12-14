from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse # Nunca deixar de importar django.http HttpRequest e HttpResponse

# Create your views here.


def home(request):
    return render(request, 'global/home.html')

