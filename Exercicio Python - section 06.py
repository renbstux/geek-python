"""
1 - Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, considerando numero maiores que 0.

for numero in range(15, 1, -3):
   print(numero)
"""

"""
2 - Escreva um programa que escreva na tela de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve usar a estrutura 
de repetição for, a segunda while, e a terceira do while.

num1 = 1
num2 = 1

for numero in range(1, 101):
    print(numero)

while num1 != 101:
    print(num1)
    num1 = num1 + 1

while num2 != 101:
    print(num2)
    num2 = num2 + 1
"""


"""
3 - Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e 
terminado em 0. Mostrar uma mensagem "FIM!" após a contagem.

numero = 10

while numero != -1:
    print(numero)
    numero = numero - 1

print('FIM!')
"""

"""
4 - Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o em 1000 em 1000, imprimindo o seu 
valor na tela, ate que o seu valor seja 100000(cem mil).

for numero  in range(0, 100000, 1000):
    print(type(numero))
    print(numero)
"""

"""
5 - Faça um programa que peça ao usuario para digitar 10 valores e some-os.

v1 = int(input('Insira o valor 1: '))
v2 = int(input('Insira o valor 2: '))
v3 = int(input('Insira o valor 3: '))
v4 = int(input('Insira o valor 4: '))
v5 = int(input('Insira o valor 5: '))
v6 = int(input('Insira o valor 6: '))
v7 = int(input('Insira o valor 7: '))
v8 = int(input('Insira o valor 8: '))
v9 = int(input('Insira o valor 9: '))
v10 = int(input('Insira o valor 10: '))
total = (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10)
print(f'O Valor Total é: {total} ')

"""
"""
6 - Faça um programa que leia 10 inteiros e imprima sua média.

v1 = int(input('Insira o valor 1: '))
v2 = int(input('Insira o valor 2: '))
v3 = int(input('Insira o valor 3: '))
v4 = int(input('Insira o valor 4: '))
v5 = int(input('Insira o valor 5: '))
v6 = int(input('Insira o valor 6: '))
v7 = int(input('Insira o valor 7: '))
v8 = int(input('Insira o valor 8: '))
v9 = int(input('Insira o valor 9: '))
v10 = int(input('Insira o valor 10: '))
total = (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10)
print(f'O Valor Total é: {total/10} ')

"""
"""
7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos e imprima a sua media.

v1 = int(input('Insira o valor 1: '))
if v1 < 0:
    v1 = 0
v2 = int(input('Insira o valor 2: '))
if v2 < 0:
    v2 = 0
v3 = int(input('Insira o valor 3: '))
if v3 < 0:
    v3 = 0
v4 = int(input('Insira o valor 4: '))
if v4 < 0:
    v4 = 0
v5 = int(input('Insira o valor 5: '))
if v5 < 0:
    v5 = 0
v6 = int(input('Insira o valor 6: '))
if v6 < 0:
    v6 = 0
v7 = int(input('Insira o valor 7: '))
if v7 < 0:
    v7 = 0
v8 = int(input('Insira o valor 8: '))
if v8 < 0:
    v8 = 0
v9 = int(input('Insira o valor 9: '))
if v9 < 0:
    v9 = 0
v10 = int(input('Insira o valor 10: '))
if v10 < 0:
    v10 = 0
total = (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10)
print(f'O Valor Total é: {total/10} ')

"""
"""
8 - Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.

maior = ''
menor = ''

v1 = int(input('Insira o valor 1: '))
maior = v1
menor = v1
v2 = int(input('Insira o valor 2: '))
v3 = int(input('Insira o valor 3: '))
v4 = int(input('Insira o valor 4: '))
v5 = int(input('Insira o valor 5: '))
v6 = int(input('Insira o valor 6: '))
v7 = int(input('Insira o valor 7: '))
v8 = int(input('Insira o valor 8: '))
v9 = int(input('Insira o valor 9: '))
v10 = int(input('Insira o valor 10: '))

if v2 > v1:
    maior = v2
elif v2 < v1:
    menor = v2

if v3 > maior:
    maior = v3
elif v3 < menor:
    menor = v3

if v4 > maior:
    maior = v4
elif v3 < menor:
    menor = v4

if v5 > maior:
    maior = v5
elif v5 < menor:
    menor = v5

if v6 > maior:
    maior = v6
elif v6 < menor:
    menor = v6

if v7 > maior:
    maior = v7
elif v7 < menor:
    menor = v7

if v8 > maior:
    maior = v8
elif v8 < menor:
    menor = v8

if v9 > maior:
    maior = v9
elif v9 < menor:
    menor = v9

if v10 > maior:
    maior = v10
elif v10 < menor:
    menor = v10

print(f'O Valor maior é: {maior}')
print(f'O Valor menor é: {menor}')
"""



