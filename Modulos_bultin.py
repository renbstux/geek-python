"""
Trabalhando com modúlos Bultin ( modulos integrados, que já vem instalados no Python)

|Python|Módulos Builtin|

https://docs.python.org/3/py-modindex.html

# utilizando alias (apelidos) para módulos/funções

import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())


# Importando todo o módulo

import random

print(random.random())

# utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())
"""
# Costumamos a utilizar tuple para colocar multiplos imports de um mesmo módulo

from random import (random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(1, 9))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('Renato'))

