"""
Reversed

OBS: Não confunda com a função reverse() que estudamos na listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iteravel.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

#Tupla
print(tuple(reversed(lista)))

#Conjunto (SET)
print(set(reversed(lista))) # Set não define a ordem dos elementos

# Podemos iterar sobre o reversed()
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais facil com o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

#Apesar que também já vimo como fazer isso utilizando o proprio range()
for n in range(9, -1, -1):
    print(n)
