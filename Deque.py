"""
Modulo Collections - Deque
https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque

Podemos dizer que o DEQUE é uma lista de alta performance.

"""
# Importando

from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final

print(deq)

deq.appendleft('k')

print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o ultimo elemento

print(deq)

print(deq.popleft())    # Remove e retorna o primeiro elemento

print(deq)