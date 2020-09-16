"""
Annotations

#print(circuferencia.__annotations__)

nome: str = 'Geek University'

peso: float = 67.9

ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)

"""
import math

def circuferencia(raio: float) -> float:
    return 2 * math.pi * raio

class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando.'

p = Pessoa(nome='Geek University', idade=44, peso=104.4)

print(p.__dict__)

# print(p.__annotations__) Não tem annotations

print(p.andar.__annotations__)

print(p.__init__.__annotations__)