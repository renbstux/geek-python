"""
Loop for

Loop -> é uma estrutura de repetição.
For -> uma dessas estruturas

C ou Java
for(int i = 0; i < 10; i ++){
    // execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de Iteráveis
- String
    nome = 'Renato de Souza'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 - (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de FOR 2 - (Iterando sobre uma lista)
for numero in lista:
    print(numero)

range(valor inicial, valor final)
Obs: O valor final não é inclusive.

# Exemplo de For 3 - (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

"""
nome = 'Geek University '
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

"""
Enumerate:
 enumerate is useful for obtaining an indexed list:
 (0, 'G'), (1, 'e'), (2, 'e'), ...
(Indice, 'Valor')

for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome):  
    print(letra)
OBS.: Quando não precisamos de um valor do indice, podemos descarta-lo utilizando um underline!

for valor in enumerate(nome):
    print(valor) # se colocar [0] so traria os numeros e [1] só traria as letras. ex. (valor[1])
(0, 'G')
(1, 'e')
(2, 'e')
(3, 'k')
(4, ' ')
(5, 'U')
(6, 'n')
(7, 'i')
(8, 'v')
(9, 'e')
(10, 'r')
(11, 's')
(12, 'i')
(13, 't')
(14, 'y')

Loop - Exemplo 1

qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd+1):
    print(f'imprimindo {n}')
    
Loop - Exemplo 2
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

"""
for letra in nome:
    print(letra, end='') # Padrão do Python é /n pular uma linha se quiser alterar utilizar end='' no print

"""
TERMINAL -> Concatenação
>>> nome = 'Geek'
>>> nome + 'University'
'GeekUniversity'
>>> nome + ' University'
'Geek University'
>>> nome
'Geek'
>>> nome * 3
'GeekGeekGeek'
>>> nome * 30
'GeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeek'
>>> nome * 300
'GeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGe
ekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekG
eekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGee
kGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGe
ekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekG
eekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeek
GeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGee
kGeekGeekGeekGeekGeekGeek'
>>>

for num in range(1, 11):
    print(f'{nome * num}')

"""

# Original : U+1F60D
# Modificado : U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F64D' * num)