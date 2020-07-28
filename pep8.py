"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem python

The Zen of Python

import this

A Ideia do PEP8 que possamos escrever codigos Python de forma Pythonica
[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variaveis

def soma():
    pass

def soma_dois()
    pass

[3] - Utilize 4 espaços para identação! (NÃO use TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco;

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings
# e antes de constantes ou variaveis globais.

[6] - Espaços em expressões e instruções

#não Faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

#Não Faça:

algo (1)

# Faça:

algo(1)

# Não Faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não Faça:

x                    = 1
y                    = 3
variavel_longa       = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this

