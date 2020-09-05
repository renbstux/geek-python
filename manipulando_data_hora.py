"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime


import datetime

print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now()) # 2020-09-05 10:54:13.394297

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now())) # Metodo repr - representação

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 hours, 0 minute, 0 second
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)


# Recebendo dados do usuario e convertendo para data

import datetime

evento = datetime.datetime(2021, 1, 1, 0)

print(type(evento))

print(type('31/12/2020'))

print(evento)

nascimento = input('Informe sua data de nascimento(dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(type(nascimento))

print(nascimento)
"""
import datetime

evento = datetime.datetime.now()

# Acesso individual os elementos de data e hora

print(evento.year)  # ano
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.second)
print(evento.microsecond)

print(dir(evento))
