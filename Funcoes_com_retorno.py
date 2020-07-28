"""
Funções com retorno

numeros = [1, 2, 3]

ret = numeros.pop()

print(f'Retorno de pop: {ret}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

# Exemplo função
def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')

OBS: funções Python que retornam valores, devem retornar estes valores com a
palavra reservada return

OBS: Não precisamos necessariamente criar uma variavel para receber o retorno
de uma função. Podemos passar a execução da função para outras funções.

# Vamos refatorar esta função para que ela retorne o valor
def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receberr o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi '

print(diz_oi())

alguem = 'Pedro!'

print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi!'
    print('Estou sendo executado apos o retorno...')

print(diz_oi())

# Exemplo 2 - Podemos ter, em uma função, diferentes returns

def nova_funcao():
    variavel = False # True/False/None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao() # Nessa forma desempacota a tupla
print(num1, num2, num3, num4)

print(outra_funcao()) # nessa forma mostra em forma de tupla
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import random # Pacote e a função a ser a importada

def joga_moeda():
    # gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara!'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessaria.

def eh_impar():
    numero = 8
    if numero % 2 != 0: # % 2 - Modulo de 2 for diferente de 0
        return True
    return False # Não ha necessidade do Else para esta função

print(eh_impar())
"""






