"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DO USUARIO DEVE SER TRATADA!

OBS: A função do usuario é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto, esperado um numero inteiro!')
else:
    print(f'Vocé digitou {num}')

# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

#OBS: O Bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro numero: '))
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O Valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto!')


# Exemplo mais complexo CORRETO - Generico
# OBS: Você é responsavel pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema!'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))


# Exemplo mais complexo CORRETO - Semi-Generico
# OBS: Você é responsavel pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))
"""




