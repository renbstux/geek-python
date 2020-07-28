"""
Utilizando Lambdas

Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anonimas.

# função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# expressão Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão Lambda?

calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))


#  Podemos ter expressões Lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title() # Strip tira o espaço

print(nome_completo(' renato ', ' de souza '))
print(nome_completo(' melissa ', ' luz de souza '))


# Em funções Python podemos ter nenhuma ou varias entradas. Em Lambdas também

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressao>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS: Se passarmos mais argumentos do que parametros esperados teremos TypeError

# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clark', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # Ordenando pelo sobrenome - terminal [].sort(help)
print(autores)

"""
# função Quadratica
#f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))