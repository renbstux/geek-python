"""
pip install mypy

para testar

mypy nomedoprograma.py

# Correct

text: str

# incorrect

text:str

text : str

# Correct

) -> str

# Incorrect
)->str
) ->str

# Correct

alinhamento: bool = True

# Incorrect

alinhamento:bool=True
alinhamento : bool = True
alinhamento : bool=True
alinhamento: bool= True

"""
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento=False))

