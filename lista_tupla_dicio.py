lista1 = ['pizza', 'pao']
lista2 = ['macarrao', 'panqueca']
# junta as listas
lista1.extend(lista2)
# Add arroz na posicao 1
lista2.insert(1, 'arroz')
# Conta quantas vezes aparece
lista2.count('arroz')
# Remove item da lista por posicao (pop) no remove é por conteudo
lista2.pop(1)
# lista2.remove('panqueca')
print(lista2)

# dicionario = ['nome','sobrenome'] dicionario é um vetor indexado
d1 = {}
d1 = {'nome': 'inara', 'sobrenome': 'valim', 'idade': 20, 'altura': 1.60}
# nome de chaves
d1.keys()
# traz tuplas com indice e conteudo
d1.items()
d1.values()
# Remove chave
d1.pop('altura')
print(d1)
