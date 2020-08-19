"""
POO - Herança(Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa
a herdar atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionarios
    - nome
    - sobrenome
    - cpf
    - matricula

Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos e metodos comuns a outras
entidades.

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

cli1 = Cliente('Renato', 'Souza', '123.456.789-00', 5000)
fun1 = Funcionario('Felicity', 'Jones', '333.444.555-66', 1001) 

print(cli1.nome_completo())
print(fun1.nome_completo())

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada!

Quando uma classe herda de outra classe, a classe herdada por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe:
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Especifica;


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    #Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Foma não comum de acessar dados da super classe
        self.__renda = renda
   
class Funcionario(Pessoa):
    #Funcionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma mais comum de acessar a Super Classe
        self.__matricula = matricula

    
cli1 = Cliente('Renato', 'Souza', '123.456.789-00', 5000)
fun1 = Funcionario('Felicity', 'Jones', '333.444.555-66', 1001) 

print(cli1.nome_completo())
print(fun1.nome_completo())

print(cli1.__dict__)
# {'_Pessoa__nome': 'Renato', '_Pessoa__sobrenome': 'Souza', '_Pessoa__cpf': '123.456.789-00', '_Cliente__renda': 5000}
print(fun1.__dict__)


# Sobrescrita de Métodos (Overriding)    

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe 
em classes filhas.

"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Foma não comum de acessar dados da super classe
        self.__renda = renda
   
class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf) # Forma mais comum de acessar a Super Classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario Matricula: {self.__matricula} Nome: {self._Pessoa__nome}'

cli1 = Cliente('Renato', 'Souza', '123.456.789-00', 5000)
fun1 = Funcionario('Felicity', 'Jones', '333.444.555-66', 1001) 

print(cli1.nome_completo())
print(fun1.nome_completo())


