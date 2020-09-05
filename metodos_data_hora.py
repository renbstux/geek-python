"""
Métodos de Data e Hora

import datetime
# Com now() podemos especificar um timezone (Fuso Horario)
agora = datetime.datetime.now()  #now == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()  #today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

import datetime

# mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))


import datetime

# Encontrar o dia de semana. weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira

# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())



import datetime

aniversario = input('Qual a sua data de nascimento? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um Domingo')


import datetime

# Formatando datas/horas com strftime() (String Format Time)

hoje = datetime.date.today()

print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)

-----------------------------------------------------------------------------------------
import datetime

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'

# Formatando datas/horas com strftime() (String Format Time)

hoje = datetime.date.today()

print(formata_data(hoje))

-------------------------------------------------------------------
pip install textblob

https://textblob.readthedocs.io/en/dev/

# TextBlob não é recomendado pois necessita da internet para traduzir o texto de Inglês para qualquer linguagem

import datetime
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.date.today()

print(formata_data(hoje))
-----------------------------------------------------------------------------------------------------

# Usando o strptime, não confundir com strftime
import datetime

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

------------------------------------------------------------------------------------------------------------

# Somente a hora

almoco = datetime.time(12, 30, 0)

------------------------------------------------------------------------------------------------------------

import timeit

# Marcando tempo de execução do nosso codigo com o timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(type(tempo))
print(tempo)

# list Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(type(tempo))
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(type(tempo))
print(tempo)

"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))