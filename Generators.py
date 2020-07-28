"""
Generators Expression

Em Aulas anteriores nós estudamos:
- List Comprehensions;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension...porque elas se chamam Generators

nome = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nome])

# Poderiamos ter feito utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


# Qual é a utilidade de getsizeof()? -> Retorna a quantidade bytes em mem do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string/valores real/Boolean estão ocupando em memória.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(9234565765767868))

print(getsizeof(True))


from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

#Gerando uma lista de numeros com Generators
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria:  ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')
"""
# Eu posso iterar no Generator Expression? SIM!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)




