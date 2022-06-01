from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from.models import Receita


def index(request):

    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    # o receitas_all é utilizado na página HTML, Exemplo: {% for receita in receitas_all %}
    dados={
        'receitas_all':receitas
    }

    return render(request, 'index.html', dados)



def receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id)

    # o receitas é utilizado na página HTML, Exemplo: {{receitas.nome_receita}}
    receita_a_exibir = {
        'receitas':receita
    }

    return render(request,'receita.html', receita_a_exibir)