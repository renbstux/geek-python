"""
Reduce

OBS: A partir do Python 3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% da vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parametros:

def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parametros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    passo 2: res2 = f(res1, 03) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(rensm, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""

# Como funciona na pratica?

# vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nos precisamos de uma função que receba dois parametros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)