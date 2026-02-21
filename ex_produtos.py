'''Exercício da aula 162'''
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy
from pprint import pprint as pp

novos_produtos=copy.deepcopy(produtos)
pp('Lista de produtos')
pp(produtos)
pp('\n')

for i in range(len(novos_produtos)):
    novos_produtos[i]['preco']=(novos_produtos[i]['preco']//10)+novos_produtos[i]['preco']
pp('Novos produtos com aumento de 10%')
pp(novos_produtos)
pp('\n')

pp('Produtos ordenados por nome decrescente')
produtos_ordenados=copy.deepcopy(novos_produtos)
produtos_ordenados=sorted(produtos_ordenados, key=lambda p: p['preco'], reverse=True )
pp(produtos_ordenados)
pp('\n')

pp('Produtos ordenados por preço crescente')
produtos_ordenados_por_preco=copy.deepcopy(produtos_ordenados)
produtos_ordenados_por_preco=sorted(produtos_ordenados_por_preco, key=lambda p: p['preco'], reverse=False)
pp(produtos_ordenados_por_preco)