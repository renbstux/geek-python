"""
Len, Abs, Sum, Round

# Len

len() -> retorna o tamanho (ou seja, o numero de itens) de um iterável.

# Só para revisar

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 100)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())


# Abs

abs() -> retorna o valor absoluto de um numero inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# Sum

sum() -> recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial

#OBS: O valor inicial default = 0

# Exemplos Sum
print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5)) # O valor inicial 5 foi informado em separado, por default é 0

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4, 5))) # Tupla

print(sum({1, 2, 3, 4, 5})) # Set

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values())) # .values() faz com que o dicionario seja somado somente os valores!


# Round

round() -> retorna um numero arrendondado para n digito de precisão após a casa decimal. Se a precisão não for
informado retorna o inteiro mais próximo
"""

# Exemplos Round

print(round(10.2)) # retorna Inteiros

print(round(10.5))

print(round(10.6))

print(round(1.211212121212, 2)) # 2 do final informa a quant. de casa decimal

print(round(1.21999999999, 2)) # Retorna o valor Real











