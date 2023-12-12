from django.urls import path
from app_recipes.views import home, sobre, contato, historia # Cada página criada deve ser importada.


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('historia/', historia),
]
