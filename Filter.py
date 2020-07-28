"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


valores = 1, 2, 3, 4, 5, 6 # Tupla com () ou não

media = sum(valores) / len(valores)# sun=Soma / len=quantidades de elementos

print(media)


# Biblioteca para trabalhar com dados estatisticos
import statistics

#Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean() - Mean é media
media = statistics.mean(dados)

print(f'A Média é: {media}')
#OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(type(res)) #<class 'filter'>
print(list(res))

print(f'Novamente: {list(res)}') # Os dados são armazenados e mostrados somente uma unica vez!

#OBS: Assim como na função map(), após serem utilizados dos dados de filter() eles são excluidos da memória.


paises = ['', 'Argentina', '', 'Brasil', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))


paises = ['', 'Argentina', '', 'Brasil', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

#res = filter(lambda pais:len(pais) > 0, paises)
#res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é

# map() -> recebe dois parametros, uma função é um iterável e retorna um objeto mapeando a função para cada elemento
# do iterável.

# filter() -> Recebe dois parametros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
# de acordo com a função.

# A grande diferença é função , filter() sempre retorna True or False, no map() sempre retorna outros valores


# Exemplo mais complexo

usuarios = [
    {"username": "samuel", 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {"username": "carla", 'tweets': ['Eu amo meu gato']},
    {"username": "jeff", 'tweets': []},
    {"username": "bob123", 'tweets': []},
    {"username": "doggo", 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
    {"username": "gal", 'tweets': []}
] # List
print(usuarios)
# Filtras os usuarios que estão inativos no Twitter

# Forma 1
#inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))

print(inativos)

# Uma lista vazia em boolean é False
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres

lista= list(map(lambda nome: f'Sua Instrutora é {nome}', filter(lambda nome: len(nome) <= 5, nomes)))

print(lista)