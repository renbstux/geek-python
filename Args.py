"""
Entendendo o *args

 - o *args é um parametro, como outro qualquer. Isso significa que você poderá
 chamar de qualquer coisa, desde que comece com asterisco.

 Exemplo:

 *xis

 Mas por convenção, utilizamos *args para defini-lo

 Mas o que é o *args?

 O parametro *args utilizado em uma função, coloca os valores extras informados como entradas em uma tupla. Então
 desde já lembre-se que tuplas são imutáveis.

 # Exemplo

def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(5, 6))

print(soma_todos_numeros(4, 6, 9, 5)) #TypeError

Exemplo 1
def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é ...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7] # tupla

# Desempacotador utilizando o asterisco

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento
# uma coleção de dados. Desta forma, ele saberá que precisará antes desempacotar estes dados