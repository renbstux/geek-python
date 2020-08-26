"""
POO - Herança Múltipla - Multiple Inherintance 

Herança múltipla, em orientação a objetos, é o conceito de herança de duas ou mais classes. 
Ela é implementada nas linguagens de programação C++ e em Python, por exemplo. 
A linguagem Java possui apenas herança simples, mas permite que uma classe implemente várias interfaces. 

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e metodos de todas as classe herdadas.

OBS: A herança multipla pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 3 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

OBS: Não importa se a derivação é direta ou indireta. A Classe que realizar a Herança herdará
todos os atributos e métodos das super classe.


"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
        
    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar()) # Eu sou Tux da terra! Method Resolution Order - MRO

# Objeto é uma instância de 

print(f'Tux é instancia de Pinguim? {isinstance(pinguim, Pinguim)}') # True
print(f'Tux é instancia de Aquatico? {isinstance(pinguim, Aquatico)}') # True
print(f'Tux é instancia de Terrestre? {isinstance(pinguim, Terrestre)}') # True
print(f'Tux é instancia de Object? {isinstance(pinguim, object)}') # True
print(f'Tux é instancia de Animal? {isinstance(pinguim, Animal)}') # True