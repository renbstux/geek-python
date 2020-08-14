"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos 
nos conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instancia;
    - Atributos de classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do metodo construtor.

OBS: Metodo construtor: É um metodo especial utilizado para a construção do objeto.


# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico.
Ou seja, pode ser acessado em todo projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da propria classe onde está declarado,
utiliza-se __ duplo undescore no inicio do seu nome.

Isso é conhecido também como Name Mangling.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

#print(user.__senha) # AttributeError

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não 
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

print(dir(user))
# '_Acesso__senha'

print(user._Acesso__senha) # Temos acesso. Mas nao deveriamos fazer este acesso.(Name Mangling)


user.mostra_senha()

user.mostra_email()

# O que significa atributos de instancia?

# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '12345678')

user1.mostra_email()
user2.mostra_email()

p1 = Produto('Playstation 5', 'Video Game', 5000.00)
p2 = Produto('Xbox S', 'Video Game', 4500.00)

print(p1.valor) # Acesso possivel, mas incorreto de um atributo de classe
print(p2.valor) # Acesso possivel, mas incorreto de um atributo de classe

# OBS: Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;


# Atributos de Classe


# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre
# todas as instancias da classe. Ou seja, ao inves de cada instancia da classe ter seus proprios
# valores como é o caso dos atributos de instancia, com os atributos de classe todas as instancias
# terão o mesmo valor para este atributo.

# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id
"""
# Classes com Atributo de Instancia Publico

class Lampada: # Atributo voltagem do objeto lampada vai receber voltagem...
    
    def __init__(self, voltagem, cor): # Metodo construtor __init__
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos publicos e Atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Refatorar a classe Produto

class Produto:

    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinâmicos -> Um atributo de instancia que pode ser criado em tempo de execução.

# OBS: O atributo dinamico será exclusivo da instancia que o criou.

p1 = Produto('Playstation 5', 'Video Game', 5000.00)
p2 = Produto('Arroz', 'Mercearia', 5.99)

p2.peso = '5Kg' # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor R$: {p2.valor}, Peso: {p2.peso}')
print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor R$: {p1.valor}, Peso: {p1.peso}')