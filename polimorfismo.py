"""
POO - Polimorfismo

Poli -> Muitos ou Muitas
Morfis -> Formas

Quando reimplementamos um método presente na classe pai em classes filhas
estamos realizando um sobrescrita de método (Overriding).

o Overriding é a melhor representação do polimorfismo.

"""

class Animal(): # Por padrão todas as class herdam de object

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método') # raise Exceção

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Wau Wau')

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Miau')

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo...')

# Testes

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()