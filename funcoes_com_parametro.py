"""
Funções com Parâmetro (de Entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refatorando a função
def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nesta dara querida')
    print('Muitas felicidades')
    print('Muitos Anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Melissa')

# funções podem ter n parametros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parametros forem necessario. Eles são separadas por virgula.

# exemplo

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 1, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se informar um numero errado de parametros ou argumentos, teremos TypeError

# Nomeando parametros

def nome_completo(nome, sobrenome): # Parametros - (nome, sobrenome)
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie')) # Argumento

# A diferença entre parametros e Argumentos

# Parâmentros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
"""

# Erro comum na utilização do return

def soma_impares(numero):
    total = 0
    for num in numero:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))





