"""
Argumentos somente Posicionais

valor = '67.3'
print(float(valor))

def cumprimenta_v1(nome):
    return f'Olá {nome}'

print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))

________________________________________________
def cumprimenta_v2(nome, /):
    return f'Olá {nome}'

print(cumprimenta_v2('Geek'))
print(cumprimenta_v2(nome='Geek'))
___________________________________________________

def cumprimenta_v3(nome, /, mensagem='Ola'):
    return f'{mensagem} {nome}'

print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-Vinda'))
________________________________________________________________________
def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'

print(cumprimenta_v4('Geek'))
print(cumprimenta_v4('Felicity', 'Bem-Vinda'))
print(cumprimenta_v4('University', mensagem='Hello')) # some positional-only arguments passed as keyword arguments: 'mensagem'
__________________________________________________________________________
def cumprimenta_v5(*, nome):
    return f'Olá {nome}'

print(cumprimenta_v5(nome='Geek'))
print(cumprimenta_v5('Geek'))
___________________________________________________________________________
* Obrigatorio informar a variavel
/ obrigatorio informar o valor
"""
def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'

print(cumprimentar_v6('Geek', mensagem1='Hello', mensagem2='Tenha um bom dia!'))
print(cumprimentar_v6('Geek', mensagem2='Tenha uma bom dia!'))
print(cumprimentar_v6('Geek', 'Oi', mensagem2='Vamos?'))



