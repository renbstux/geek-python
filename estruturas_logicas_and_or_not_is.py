"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    -not , is
Operadores binarios:
    -and, or

Regras de Funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro precisam ser True
ativo = False
logado = False

if ativo or logado:
    print('Bem Vindo Usuario!')
else:
    print('Você Precisa ativar sua conta. Por Favor, cheque seu e-mail')

Para o 'not', o valor do booleano o valor é invertido, ou seja, se for true, vira false ou vice-versa.
ativo = True
logado = False

# Se não estiver ativo
if not ativo:
    print('Você Precisa ativar sua conta. Por Favor, cheque seu e-mail')
else:
    print('Bem Vindo Usuario!')

#print(not False)

Para 'is' o valor é comparado com um segundo.

TERMINAL PYTHON
>>> nome = 'Geek'
>>> dir(nome)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capital
ize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', '
swapcase', 'title', 'translate', 'upper', 'zfill']
>>> nome.isupper()
False
>>> nome.istitle()
True

"""

ativo = True
logado = False

# Se não estiver ativo
if ativo:
    print('Bem Vindo Usuario!')
else:
    print('Você Precisa ativar sua conta. Por Favor, cheque seu e-mail')

#print(not False)
#Ativo é False
print(ativo is True)


