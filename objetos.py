"""
POO - Objetos

Objetos -> São instancias da classe. Ou Seja, após o mapeamento do objeto do mundo real para sua representacao
computacional, devemos poder criar quantos objetos forem necessarios. Podemos pensar nos objetos/instancias
de uma classe como variaveis do tipo definido na classe.

# Instâncias/Objetos
lamp1 = Lampada('Branco', '220V', '4000KV')

lamp1.ligar_desligar()

print(f' A Lâmpada está ligada? {lamp1.checa_lampada()}')

ccs = ContaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O Cliente {self.__nome} diz OI!')
        

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

    def mostra_cpf(self):
        print(f'O CPF do cliente {self.__cliente._Cliente__nome} é {self.__cliente._Cliente__cpf} ')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

cli1 = Cliente('Angelina Jolie', '123.456.789-99')

cc = ContaCorrente(5000, 10000, cli1)

cc.mostra_cliente()
cc.mostra_cpf()

cc._ContaCorrente__cliente.diz()