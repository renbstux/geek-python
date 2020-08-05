"""
Teste de Velocidade com Expressões Geradoras

# Generators(Geradores)

def nums():
    for num in range(1, 11):
        yield num

ge1 = nums()

print(ge1) # Generator <generator object nums

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1, 11))

print(ge2) # Generator Expression <generator object <genexpr>

print(next(ge2))
print(next(ge2))
"""


# Realizando o teste de velocidade

import time

#Generator Expression 

gen_inicio = time.time()
print(sum(num for num in range(10000000))) # 10 Milhoes
gen_tempo = time.time() - gen_inicio

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(10000000)])) # 10 Milhoes
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')