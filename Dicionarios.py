"""
Dicionarios

Obs.: Em algumas linguagens de programação, os dicionarios Python são conhecidos
por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionários são representados pro chaves {}.

print(type({}))

OBS: Sobre o dicionários
 - Chave e valor são separados por dois pontos 'chave:valor';
 - Tanto chave quanto valor podem ser de qualquer tipo de dado;
 - Podemos misturar tipos de dados;

 # Criação de dicionários

# Forma 1 (Mais Comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos Comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando Elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# Caso tentantos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

OBS: O tipo None em Python é sempre considerado False

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Caso o get não encontre o bojeto com a chave informada será retornado o valor None e não será gerado
# KeyError
pais = paises.get('ru')

if pais:
    print(f'Encontrei o País {pais}')
else:
    print('Não encontrei o País')


paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Podemos definir um valor padrão para caso não encontramos o objeto com a chave informada
pais = paises.get('py', 'Não Encontrado')

if pais:
    print(f'Encontrei o País {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado,( int, float, string, boolean) , inclusive lista, tupla dicionario,
# Como chaves de dicionarios.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionarios,
# pois as mesmas são imutaveis!

localidade = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em New York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidade)
print(type(localidade))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais Comum

receita['abr'] = 350

print(receita)

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# CONCLUSÃO 2: Em dicionarios, NÂO podemos ter chaves repetidas.


#  Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)

print(receita)

#OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento um KeyError é retornado.
#OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado

# Forma 2 - Menos comum

del receita['fev']

print(receita)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado.


# Imagine que você tem um comercio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - Quantidade;
        - preço
    Produto 2:
        - nome;
        - Quantidade;
        - preço



# 1 - Poderiamos utilizar uma lista para isso? SIM

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? SIM

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o indice de cada informação no produto.

# 3 - Poderiamos utilizar um Dicionario para isso? SIM
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho em cada produto
# podemos ter certeza sobre cada informação.

>>> dir({})
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__h
ash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '
__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'updat
e', 'values']

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (Zerar Dados)

d.clear()

print(d)

# Copiando um dicionario para outro

# forma 1 - Deep Copy

novo = d.copy()  # Deep Copy

print(novo)

novo['d'] = 4

print(d)
print(novo)

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#OBS: o método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor') # Em dicionarios chave não pode ser duplicadas
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)


"""





