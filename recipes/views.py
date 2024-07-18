from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
Essa função renderiza um arquivo html que está dentro de 
recipes/templaes/home.html.
'''
def home(request):
    return render(request, 'recipes/home.html')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')
