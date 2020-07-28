"""
List Comprehension

 - Utilizando List comprehension nós podemos gerar novas listas com dados processados a partir de outro iteravel.

 # Sintaxe da List Comprehension

[ dado for dado in iterável ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)
"""
"""
Para entender melhor o que esta acontecendo devemos dividir a expressão em duas partes:

- A Primeira parte: for numero in numeros
- A segunda parte: numero * 10

res = [numero /2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehension versos Loop
# loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = ()

for numero in numeros:
    numeros_dobrados = numero * 2
    numeros_dobrados.append(numeros_dobrados)

print(numeros_dobrados)


# List Comprehension
numeros = [1, 2, 3, 4, 5]

print([numero * 2 for numero in numeros])
"""
# Outros exemplos

# 1
nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'melissa', 'priscila', 'renato']

print([caixa_alta(amigo) for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3, 14]])

#5

print([str(numero) for numero in [1, 2, 3, 4, 5]])