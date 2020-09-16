"""
PEP 484 - Python 3.5 >

def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

print(cumprimentar('Geek'))



def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))
"""



