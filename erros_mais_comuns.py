"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece coomo parte da linguagem.

# Exemplo SyntaxError

a)
def funcao:
    print('Geek University')

b)
def = 1
None = 1

c)
return


2 - NameError -> Ocorre quando uma variável ou função não foi definida.

# Exemplo NameError

a)
print(Geek) # NameError: name 'Geek' is not defined

b)
geek()

c)
a = 18
OBs: para corrigir seria somente declarar ela globalmente antes de iniciar - msg = 'Menor que 10'
if a < 10:
    msg = 'É maior que 10'

print(msg)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplo TypeError

a)
print(len(5)) # TypeError: object of type 'int' has no len()

b)
print('Geek' + []) # TypeError: can only concatenate str (not "list") to str

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
indice inválido.

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2]) # IndexError: list index out of range

lista = ['Geek']
print(lista[0][10]) # IndexError: string index out of range


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado.

Exemplos ValueError

a)
print(int('Geek')) # ValueError: invalid literal for int() with base 10: 'Geek'


6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

Exemplos KeyError

a)
dic = {'Python': 'University'}
print(dic['Geek']) # KeyError: 'Geek'


7 - AttributeError -> Ocorre quando uma variavel não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 4)
print(tuple.sort()) # AttributeError: type object 'tuple' has no attribute 'sort'


8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 Espaços)

Exemplo IndentationError

a)
def nova():
print('Geek') # IndentationError: expected an indented block

b)
for i in range(10):
i + 1 # IndentationError: expected an indented block

OBS: Exceptions e Error são sinonimos na programação.

OBS: Importante ler e prestar atenção na saída de erro.
"""







