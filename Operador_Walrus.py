"""
O Operador Walrus permite fazer a atribuição e retorno de valor em unica expressão.

variavel := expressao

nome = 'Geek University'
print(nome)

print(nome := 'Geek University')


cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'Jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')
"""
# Python 3.8

cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
