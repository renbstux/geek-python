"""
Geradores 

- Geradores (Generators) são Iterators (iteradores)

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:

- Generatos podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre funções e Generator Functions (Funções Geradoras)

------------------------------------------------------------------------------------------------
| Funções                                             | Generator Functions                    |
------------------------------------------------------------------------------------------------
| utilizam return                                     | utilizam yield                         |
------------------------------------------------------------------------------------------------
| retorna uma vez                                     | podem utilizar yield multiplas vezes   |
------------------------------------------------------------------------------------------------
| quando executada, retorna um valor                  | quando executada, retorna um generator |
------------------------------------------------------------------------------------------------

# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: Uma Generator Function não é um Generator. Ela gera um Generator. ok?

gen = conta_ate(5)

#print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: Uma Generator Function não é um Generator. Ela gera um Generator. ok?

gen = conta_ate(10)

for num in gen:
    print(num)


# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: Uma Generator Function não é um Generator. Ela gera um Generator. ok?

gen = conta_ate(10)

print(next(gen)) # 1

print('Geek')

for num in gen:
    print(num)
"""
# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#OBS: Uma Generator Function não é um Generator. Ela gera um Generator. ok?

gen = list(conta_ate(10))

print(gen)