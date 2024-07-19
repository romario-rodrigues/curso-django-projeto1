from django.shortcuts import render


# Create your views here.

'''
Essa função renderiza um arquivo html que está dentro de 
recipes/templaes/home.html.
'''
def home(request):
    return render(request, 'recipes/pages/home.html')

