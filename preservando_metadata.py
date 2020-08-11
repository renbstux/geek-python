"""
Preservando metadatas com wraps

Metadatas -> são dados intrísecos em arquivos.

Wraps -> São funções que envolvem elementos com diversas finalidades.



# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        Eu sou uma função(logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}') # __name__ retorna o nome da função, no caso soma
        print(f'Aqui a documentação: {funcao.__doc__}')# __doc__ retorna a documentação inserida para a funçao
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    Soma dois numeros.
    return a + b 

#print(soma(10, 30))

print(soma.__name__) # soma
print(soma.__doc__) # Soma dois numeros
"""

#  Resolução do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função(logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}') # __name__ retorna o nome da função, no caso soma
        print(f'Aqui a documentação: {funcao.__doc__}')# __doc__ retorna a documentação inserida para a funçao
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros."""
    return a + b 

#print(soma(10, 30))

print(soma.__name__) # soma
print(soma.__doc__) # Soma dois numeros

print(help(soma))
