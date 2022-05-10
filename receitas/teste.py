receitas = {
    1:'receita 1',
    2:'receita 2',
    3:'receita 3'
}
descricoes = {
    1:'descrição 1',
    2:'descrição 2',
    3:'descrição 3'
}

dados ={
    'nome_das_receitas': receitas,
    'descricoes_receitas':descricoes
}

print(type(receitas))
print(dict(receitas))
print('===[Lista de Receitas]===')
for chave, receita in receitas.items():
    print(f'Chave = {chave} - Receita = {receita}')

