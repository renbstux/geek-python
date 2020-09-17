"""Não utilizar se possivel"""

import math

def circuferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

#print(circuferencia(8))

#print(circuferencia(12.5))

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

def cabecalho2(
        texto,  # type: str
        alinhamento=True  # Type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)

nome = 'Geek University'  # type: str