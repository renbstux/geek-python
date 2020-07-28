"""
Módulo Random e o que são módulos?

 - Em Python, módulos nada mais são do que outros arquivos Python.

 Módulo Random -> Possui varias funções para geração de números pseudo-aleatorio.

Terminal:
import random
dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loa
der__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sq
rt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate
', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# random() -> Gera um numero real pseudo-aleatorio entre 0 e 1.

#OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo. ( Não recomendado!)

import random

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do modulo ficarão disponiveis ( Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremis uma forma melhor na Forma 2

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do modulo random.

# Forma 2 - Importando uma função especifica do módulo (Forma Recomendada!)

from random import random

# No import acima, estamos falando: Do modulo random, importe a função random()

for i in range(10):
    print(random())

# uniform() -> Gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10)) # 10 não é incluido

# randint() -> Gera valores pseudo-aleatorios entre os valores estabelecidos.

#  Gerador de apostas para a Mega-Sena
from random import randint

# Gerador de apostas para a Mega-Sena
for i in range(6):
    print(randint(1, 61), end=', ') # começa em 1 e vai até 60

# choice() -> Mostra um valor aleatorio entre um iteravel.
from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']

print(choice(jogadas))
"""

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas.pop())











