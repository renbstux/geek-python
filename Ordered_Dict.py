"""
Módulo Collections: Ordered Dict

Terminal
help({})

# Em um dicionario, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

chave=a:valor=1
chave=b:valor=2
chave=c:valor=3
chave=d:valor=4
chave=e:valor=5

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


"""
from _collections import OrderedDict

# Entendo a diferença entre Dict e Ordered Dict
# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True/False???

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # True/False???


