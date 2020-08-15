"""
POO - Metodos

 - Metodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
 realizar no seu sistema.

 Em Python, dividimos os métodos em 2 grupos: Métodos de intância e Métodos de Classe.

 # Metodos de Instancia

O Método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto
a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder(Double Underline)

Os Métodos/Funções dunder em Python são chamados de métodos mágicos

ATENÇÃO! Por mais que possamos criar nossas funções utilizando dunder não é aconselhado.
Python possui vários métodos com está forma de nomeclatura e pode ser mudemos o comportamento dessas funções
mágicas internas da linguagem. Então, evite ao máximo. De preferencia nunca o faça!


# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por
underline.


p1 = Produto('Playstation 4', 'Video Game', 2300.00)

print(p1.desconto(50))

print(Produto.desconto(p1, 40)) # p1 nesse caso seria self ou seja o objeto em si,  e o valor do desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(Usuario.nome_completo(user1)) # Nesse caso passamos a instancia e o user1 é o self
print(user2.nome_completo())

print(f'Senha User1: {user1._Usuario__senha}') # Acesso de forma errada de um atributo de classe
print(f'Senha User2: {user2._Usuario__senha}') # Acesso de forma errada de um atributo de classe
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        '''Retorna o valor do produto com desconto'''
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('Informe o nome:')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o seu e-mail: ')
senha = input('Informe a sua senha: ')
confirma_senha = input('Confirme a sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não Confere!')
    exit(1)

print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') # Acesso Errado