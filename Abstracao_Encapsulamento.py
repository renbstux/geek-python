"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso codigo dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> cápsula

# Relembrando Atributos/Métodos são privados em Python

Imagina que termos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso 
fora da classe. Com Python acontece um fenomeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.


Forma Publica

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

# Testando

conta1 = Conta('Geek', 150.00, 1500.00)

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

# PERIGO - Por usar atributos publicos

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 999999999999999999999999
conta1.limite = 99999999999999999999999999999999999999999

print(conta1.__dict__)

conta1.extrato()


# Testando Privado

conta1 = Conta('Geek', 150.00, 1500.00)

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular) #Name Mangling - Lembre-se - errado usar fora da Classe

conta1._Conta__titular = 'Angelina'

print(conta1.__dict__)


# Testando

conta1 = Conta('Geek', 150.00, 1500.00)

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(300)

print(conta1.__dict__)


valor = 100

conta2.sacar(valor)

conta1.depositar(valor)


"""
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O Valor precisa ser positivo!')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente!')
        else:
            print('O Valor deve ser positivo!')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferencia paga por quem realizou a transferencia

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor
        

# Testando

conta1 = Conta('Angelina', 150.00, 1500.00)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()

