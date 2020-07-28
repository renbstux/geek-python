"""
Sorted - Uma função integrada do Python

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o proprio nome diz, sorted() serve para ordenar.

OBS: O sorted() SEMPRE retorna uma lista com os elementos do iteravel ordenados

#Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # Ordenar do menor para o maior

print(numeros)


#Exemplo 2

numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))

# Adicionando parametros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": "carla", 'tweets': ['Eu amo meu gato']},
    {"username": "jeff", 'tweets': []},
    {"username": "bob123", 'tweets': [], 'cor': 'amarelo'},
    {"username": "doggo", 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
    {"username": "gal", 'tweets': [], 'cor': 'preto', 'musica': 'rock'  }
] # List

print(usuarios)
# Ordenando pelo Username - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

#Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

# Ultimo Exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Black in Black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll, to young to die', 'tocou': 32}
]
# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))