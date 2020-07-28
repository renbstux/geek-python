"""
Debugando com PDB

PDB -> Python Debugger

Bug -> Inseto

#OBS: A utilização do print() para debugar código é uma pratica ruim.
def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))


# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com PyCharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 2))


# Exemplo com o PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variável)
# c (continua a execução - finaliza debugging
import pdb

nome = 'Renato'
sobrenome = 'de Souza'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = ' Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)


# Exemplo com o PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variável)
# c (continua a execução - finaliza debugging


nome = 'Renato'
sobrenome = 'de Souza'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = ' Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso ao invés de colocarmos o import do pdb no inicio do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# Exemplo com o PDB - Python Debugger - Exemplo 3

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# * A partir do Python 3.7, não é mais necessario importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variável)
# c (continua a execução - finaliza debugging


nome = 'Renato'
sobrenome = 'de Souza'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = ' Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso ao invés de colocarmos o import do pdb no inicio do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# OBS: Cuidado com conflitos entre nomes de variaveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Como os nomes das variaveis são os mesmos do comandos do pdb, devemos utilizar o comando "p" para imprimir
# as variaveis. Ou Seja: "p" nome_da_variavel

# Nada de colocar nomes não representativos em variaveis. Sempre optar por nomes significativos.

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""


