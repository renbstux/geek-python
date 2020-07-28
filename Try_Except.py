"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa
pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma generica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma
especifica.

# Exemplo 3 - Tratando um erro erro especifico

try:
    geek()
except NameError:
    print('Você esta utilizando uma função inexistente')

# Exemplo 3 - Tratando um erro erro especifico

try:
    geek()
except NameError:
    print('Você esta utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro erro especifico

    try:
        len(5)
    except NameError:
        print('Você esta utilizando uma função inexistente')


# Exemplo 5 - Tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    #len(4)
    #geek()
    print('Geek'[8])
except NameError as erra:
    print(f'deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('deu em erro diferente')
"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(dic, "nome"))



