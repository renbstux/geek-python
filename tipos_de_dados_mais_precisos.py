"""
int, str, float, liast, list, set, dict, etc

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro('Geek'))

- Literal Type;
- Union
- Final
- Typed Dictionaries
- Protocols

from typing import Literal

def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass
_________________________________________________________________________
def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação Invalida {operacao!r}') # !r destaca que operação foi utilizado com aspas simples

calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
calcula_v1('*', 3, 5)

________________________________________________________________________________

# Literal Type

from typing import Literal

def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação Invalida {operacao!r}') # !r destaca que operação foi utilizado com aspas simples

calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5)
_____________________________________________________________________________________
# Union

from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado
________________________________________________________________
# Final

from typing import Final

NOME: Final = 'Geek'

print(NOME)

NOME = 'University'

print(NOME)
____________________________________________________________________________
OBS: o mypy não esta reconhecendo @final nos metodos
OBS: quando colocamos o @final em um metodo as classes filhas não podem sobrescrever esse metodo
OBS: quando colocamos o @final em classes não podemos extender essa classe

from typing import final

@final
class Pessoa:
    pass

class Estudante():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')

class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')
____________________________________________________________________________________________
# Typed Dictionaries

from typing import TypedDict

class CursoPython(TypedDict):
    versao: str
    atualizacao: int

geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

# {'versao': '3.8.5', 'atualizacao': 2020} - Dicionario Tipado
___________________________________________________________________________________________


# Protocols - seguir um protocolo/regra

from typing import Protocol

class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudadndo o curso {valor.titulo}')

class Venda:
    titulo = 'Oi'

v1 = Venda()

estudar(v1)

"""
