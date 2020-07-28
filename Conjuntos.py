"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos
da Matematica.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matematica:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos(sets) e mapas(dicionarios) em Python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor existente, o mesmo
# Sera ignorado sem gerar error e não faz parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicadas, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34, 22, 44}
print(s)
print(type(s))

# Podemos iterar em set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitante em uma feira ou museu e os visitantes
# Informam manualmente a cidade de onde vieram.

# Nos adicionamos em cada cidade em uma lista Python, já que uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizontye', 'São Paulo', 'Florianopolis', 'Cuiaba', 'Campo Grande', 'Florianopolis', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantos cidades distintas, ou seja, únicas, temos:

# O que você faria? Faria um loop na lista....

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando um elementos em um conjuntos
s= {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro, simplesmente é ignorado e não é adicionado

# Remover elementos em um conjunto
s = {1, 2, 3}

# Forma 1

s.remove(3) # Isso não é indice, pois conjunto não são indexado, informamos o valor a ser removido!

print(s)

#OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(22)

print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado

s = {1, 2, 3}
print(s)

#  Copiando um conjunto para outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudandes do curso de Python e um
# contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos estudando Python também estudam Java.

# Precisamos gerar um conjunto com nome de estudantes Unicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
# {'Guilherme', 'Marcos', 'Ellen', 'Fernando', 'Ana', 'Julia', 'Gustavo', 'Pedro', 'Patricia'}

# Forma 2 - utilizando o caracter pipe |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudandes do curso de Python e um
# contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos estudando Python também estudam Java.

# Gerar um conjunto de estudantes que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
# {'Guilherme', 'Marcos', 'Pedro', 'Ellen'}

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
#{'Gustavo', 'Fernando', 'Ana'}

# Soma*, Valor Maximo*, Valor minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))


>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__',
 '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce_
_', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear',
 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_dif
ference', 'symmetric_difference_update', 'union', 'update']

"""






