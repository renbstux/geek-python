"""
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria,
mas sim de maneira especificada.

# Forma 1

range(valor_de_parada)

OBS: o valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Forma 1
for num in range(1, 11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: o valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

for num in range(4, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: o valor_de_parada não inclusive (inicio padrão 0, e passo especificado pelo usuario)

for num in range(5, 50, 5):
    print(num)

# Forma 4

range(Valor_de_inicio, valor_da_parada, passo)

OBS: o valor_de_parada não inclusive (valor_final especificado pelo usuario, e passo especificado pelo usuario)

for num in range(10, -1, -1):
    print(num)

pelo terminal para teste faça da seguinte forma:

>>> lista = list(range(10))

"""






