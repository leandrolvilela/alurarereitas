from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    receitas = {
        1:'receita 1',
        2:'receita 2',
        3:'receita 3',
        4:'receita 4'
    }

    dados={
        'nomes_das_receitas':receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request,'receita.html')