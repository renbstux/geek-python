"""
Funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINAMICOS e tambem de podermos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou Seja, nesta linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no maximo 5 valores.

Já em Python:

- Dinámico: Não possuem tamanho fixo; Ou Seja, podemos criar a lista simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou Seja, podemos colocar qualquer tipo de dados;

As lista em Python são representadas por colchetes: []

# Podemos facilmente checar se determinado valor esta contido na lista
num = 7

if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

cores = ['verde', 'amarelo', 'azul', 'branco']

# Podemos ordenar facilmente uma lista
lista1.sort()
print(lista1)

# podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista2.count("e"))

# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append


print(lista1)
lista1.append(42)
print(lista1)

# Obs: com append, nos só conseguimos adicionar um elemento por vez!
#lista1.append(1, 5, 8)

# Mas pode-se colocar uma lista dentro de outra lista. Ex.:
lista1.append([1, 5, 9])
print(lista1)

if [1, 5 , 9] in lista1:
    print('Encontrei a Lista!')
else:
    print('Não encontrei a Lista')

lista1.extend([120, 33, 190]) # Coloca cada elemento da lista como valor adicional a lista;
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial, o Mesmo sera deslocado para direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)

# podemos facilmente juntar duas lista
lista1 = lista1 + lista2
#lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma #2 - Com Slice
print(lista1[::-1])
print(lista2[::-1])

# Podemos contar quantos elementos tem na lista
print(len(lista1))
print(len(lista2))

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos facilmente remover o ultimo elemento de uma lista
# OBS: o pop não somente remove o ultimo elemento mas tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos a direita deste indice serão deslocados para a esquerda
# Se não houver elemento no indice informado, teremos o erro index error
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (Zerar a Lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos remover todos os elementos (Zerar a Lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exercicio 1

curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exercicio 2
curso = 'Progrmação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando : pega a lista6, coloca espaço entre cada elemento em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando : pega a lista6, coloca cifrão entre cada elemento em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos colocar qualquer tipo de dados em uma lista, inclusive  misturando esses dados
lista6 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 4534344545]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas

numero = [1, 2, 3, 4, 5]
print(numero)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])    # Verde
print(cores[1])    # Amarelo
print(cores[2])    # Azul
print(cores[3])    # Branco

# Fazer acesso aos elementos de forma indexada de forma inversa
# Para entender melhor o indice negativo pense na lista como um circulo o final de um elemento esta ligado
# ao inicio da lista!

print(cores[-1])    # Branco
print(cores[-2])    # Azul
print(cores[-3])    # Amarelo
print(cores[-4])    # Verde

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Lista aceita valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# outros metodos não tão importantes mas também uteis
# encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
# Em qual indice esta o valor 6
print(numeros.index(6))
# Em Qual indice esta o valor 9
print(numeros.index(9))
# print(numeros.index(19)) #Gera ValueError

# OBS: Caso não encontre esse elemento na lista, sera apresentado erro ValueError

# OBS: Retorna o indice do promeiro elemento encontrado
print(numeros.index(5))

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) #buscando a partir do indice 1
print(numeros.index(5, 2)) #buscando a partir do indice 2
print(numeros.index(5, 3)) #buscando a partir do indice 3
# OBS: Caso não encontre esse elemento na lista, sera apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) #Buscar o indice do valor 8, entre o indice 3 e 6

# Revisão de Slicing

#lista[inicio:fim:passo]
#range[inicio:fim:passo]

# Trabalhando com slice de lista com parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:]) # Começando no 1 e indo até o final

# Trabalhando com slice de lista com parametro 'fim'

print(lista[:4]) # Começando no 0 e indo até o indice 4

print(lista[1:3]) # Começando no 1 e indo até o indice 3

# Invertendo valores em lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma*, valor maximo*, valor minimo*, tamanho
# * Se os valores forem inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # Soma
print(max(lista)) # Maximo Valor
print(min(lista)) # Valor minimo
print(len(lista)) # tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(lista))

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferente de elemento na lista ou variaveis para receber os valores, teremos ValueError

# Copiando uma lista para outra( Shallow Copy e Deep Copy)

# FORMA 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram
# totalmente independentes, ou seja, modificando uma lista não afeta a outra, isso em Python se chama
# Deep Copy(copia profunda)
"""
# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista # Copia

print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para uma nova lista, mas
# após realizar modificação em uma das listas. essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado Shallow Copy.











