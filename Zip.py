"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passsados como entrada em pares.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

#  Sempre podemos gerar uma Lista, Tupla ou Dicionario

print(list(zip1)) # [(1, 4), (2, 5), (3, 6)] ele forma pares e cria uma tupla

zip1 = zip(lista1, lista2)
print(tuple(zip1)) # ((1, 4), (2, 5), (3, 6))

zip1 = zip(lista1, lista2)
print(set(zip1)) # {(2, 5), (1, 4), (3, 6)}

zip1 = zip(lista1, lista2)
print(dict(zip1)) #{1: 4, 2: 5, 3: 6}

# OBS: o zip() utiliza como parametro o menor tamanho em iterável. Isso significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))


# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados= [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*dados))) # * desempacota os elementos de uma tupla
"""
# Exemplo mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
aluno = ['maria', 'carlos', 'joao']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(aluno, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(aluno, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
