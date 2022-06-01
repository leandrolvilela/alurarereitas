from unicodedata import name
from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # o primeiro parametro da função path 'receita' aparece no endereço da URL (http://127.0.0.1:8000/receita)
    # o nome que está depois views. é a nome do método que está no views.py
    # o nome que está no name é utilizado no HTML {% url 'receita'%}
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]