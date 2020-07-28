"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem baicamente duas diferenças:

1 - As tuplas são representadas por parenteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar um tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# CUIDADO 1 : As tuplas são representadas por parenteses (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADO 2 : Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma Tupla!
print(tupla4)

print(type(tupla4))

tupla5= 4,
print(tupla5)

print(type(tupla5))

# CONCLUSÂO : Podemos concluir que tuplas são definidas pela virgula e não pelo uso de parentese

(4) -> não é TUPLA!
(4,) -> É uma TUPLA!
4, -> É uma TUPLA!

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

#OBS: Gera erro (ValueError) se colocarmos um numero diferente de elementos para desempacotar

# Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas são imutaveis!

# Soma*, Valor Maximo, Valor Minimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla2)
print(tupla1)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento esta contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek university')
print(escola)

print(escola.count('e'))


# Dicas na utilização de tuplas

# devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção


# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while 1 < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento esta na tupla

print(meses.index('Junho'))

# OBS: Caso o elemento não exista, sera gerado ValueError.

# Slicing

# tupla[inicio:fim:passo]

print(meses[0:])
print(meses[5:])
print(meses[0:4])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu codigo mais seguro*.

# Isso porque trabalhar com elementos imutáveis traz segurança para o código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
"""








