import time
from threading import Thread

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundo: {fim - inicio}')

# Tempo em segundo: 5.216136932373047