"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/ Java) possuem uma estrutura de dados chamadas de array;
    - Unidimensionais ( Arrays /Vetrores);
    - Multidimensionais (Matrizes);

Em Python nos temos as listas

numero = (1, 2, 3, 4, 5)

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)

print(type(listas))
# Como fazemos para acessar os dados?

print(listas[0][1]) # 2
print(listas[2][1]) # 8

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
"""
# Outros exemplos

# Gerando um tabuleiro/matrix 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])
