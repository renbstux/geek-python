"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]

set = {1, 2, 3, 4, 5} # Lembrete - Não aceita valores repetidos e não guarda ordenação
"""

# Exemplos

numero = {num for num in range(1, 7)}
print(numero)

# outro Exemplo

numero = {x ** 2 for x in range(10)}
print(numero)

# DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set

numero = {x: x ** 2 for x in range(10)}
print(numero)

letras = {letra for letra in 'Geek University'}

print(letras)