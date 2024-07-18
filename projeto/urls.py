"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
    
]

'''
Foi Criado um app com o comando python manage.py startapp recipes.
Depois foi migrado todas as funções para o app recipes/views.py
Criado ursl.py em recipes e foi migrado as rotas que estavam em urls
que estavam dentro de projeto.
Também foi importado em projetos/urls.py o include e adicionado a linha
path('', inclide('recipes.urls')) para apontar para as rotas que agora
estão em recipes/urls.py.
'''