from unicodedata import name
from django.urls import path
from django.views import View

from . import views

## path o primeiro parametro é referente ao endereço da URL 
# EXEMPLO: path('login_url', views.login, name='login')
# http://localhost:8000/usuarios/login_url 

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')
]