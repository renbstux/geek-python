"""
Módulo Collections - Counter

https://docs.python.org/3/library/collections.html?highlight=collections#collections.Counter

Collections -> High-perfomance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.


# Utilizando o Counter

from collections import Counter

#Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 44, 44, 66, 66, 55, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)
#<class 'collections.Counter'>
#Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 44: 2, 66: 2, 55: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias.


# Exemplo 2
from collections import Counter

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""
from collections import Counter

# Exemplo 3

texto = """ A Apollo 13 foi um voo espacial tripulado norte-americano que tinha a intenção de realizar o terceiro pouso 
tripulado na Lua. Foi lançada do Centro Espacial John F. Kennedy em 11 de abril de 1970 por um foguete Saturno V, tendo 
sido a sétima missão tripulada do Programa Apollo da NASA. A alunissagem foi abortada depois de um dos tanques de 
oxigênio do módulo de comando e serviço Odyssey ter explodido, após dois dias de viagem. Os astronautas Jim Lovell, 
John Swigert e Fred Haise conseguiram dar a volta à Lua e retornar em segurança para a Terra em 17 de abril, 
amerrissando no Oceano Pacífico. Swigert fora promovido à tripulação principal dois dias antes do lançamento, 
substituindo Ken Mattingly depois deste ter sido exposto à rubéola.

O tanque de oxigênio explodiu durante um procedimento padrão de agitação e seu conteúdo foi vazado para o espaço, por 
causa de uma ignição resultante de um curto-circuito ocasionado pelo isolamento danificado de um fio interno. 
O oxigênio era necessário não apenas para a respiração dos astronautas, mas também para gerar energia elétrica, e, 
assim, os sistemas de propulsão e suporte de vida do módulo de comando e serviço não poderiam mais operar. 
O Odyssey precisou ser desligado a fim de economizar recursos para reentrada, forçando Lovell, Swigert e Haise a 
utilizar o módulo lunar Aquarius como bote salva-vidas. """

palavras = texto.split()

#print(palavras)
res = Counter(palavras)

print(res)
# Counter({'de': 17, 'a': 7, 'e': 7, 'um': 6, 'do': 5, 'para': 5, 'foi': 3, 'o': 3, 'em': 3, 'oxigênio': 3, 'módulo': 3,
# 'Swigert': 3, 'à': 3, 'O': 3, 'A': 2, 'Apollo': 2, 'tripulado': 2, 'John': 2, 'por': 2, 'sido': 2, 'depois': 2,
# 'dos': 2, 'comando': 2, 'serviço': 2, 'Odyssey': 2, 'ter': 2, 'dois': 2, 'dias': 2, 'Lovell,': 2, 'Haise': 2,
# 'não': 2, '13': 1, 'voo': 1, 'espacial': 1, 'norte-americano': 1, 'que': 1, 'tinha': 1, 'intenção': 1, 'realizar': 1,
# 'terceiro': 1, 'pouso': 1, 'na': 1, 'Lua.': 1, 'Foi': 1, 'lançada': 1, 'Centro': 1, 'Espacial': 1, 'F.': 1,
# 'Kennedy': 1, '11': 1, 'abril': 1, '1970': 1, 'foguete': 1, 'Saturno': 1, 'V,': 1, 'tendo': 1, 'sétima': 1,
# 'missão': 1, 'tripulada': 1, 'Programa': 1, 'da': 1, 'NASA.': 1, 'alunissagem': 1, 'abortada': 1, 'tanques': 1,
# 'explodido,': 1, 'após': 1, 'viagem.': 1, 'Os': 1, 'astronautas': 1, 'Jim': 1, 'Fred': 1, 'conseguiram': 1, 'dar': 1,
# 'volta': 1, 'Lua': 1, 'retornar': 1, 'segurança': 1, 'Terra': 1, '17': 1, 'abril,': 1, 'amerrissando': 1, 'no': 1,
# 'Oceano': 1, 'Pacífico.': 1, 'fora': 1, 'promovido': 1, 'tripulação': 1, 'principal': 1, 'antes': 1, 'lançamento,': 1,
# 'substituindo': 1, 'Ken': 1, 'Mattingly': 1, 'deste': 1, 'exposto': 1, 'rubéola.': 1, 'tanque': 1, 'explodiu': 1,
# 'durante': 1, 'procedimento': 1, 'padrão': 1, 'agitação': 1, 'seu': 1, 'conteúdo': 1, 'vazado': 1, 'espaço,': 1,
# 'causa': 1, 'uma': 1, 'ignição': 1, 'resultante': 1, 'curto-circuito': 1, 'ocasionado': 1, 'pelo': 1, 'isolamento': 1,
# 'danificado': 1, 'fio': 1, 'interno.': 1, 'era': 1, 'necessário': 1, 'apenas': 1, 'respiração': 1, 'astronautas,': 1,
# 'mas': 1, 'também': 1, 'gerar': 1, 'energia': 1, 'elétrica,': 1, 'e,': 1, 'assim,': 1, 'os': 1, 'sistemas': 1,
# 'propulsão': 1, 'suporte': 1, 'vida': 1, 'poderiam': 1, 'mais': 1, 'operar.': 1, 'precisou': 1, 'ser': 1,
# 'desligado': 1, 'fim': 1, 'economizar': 1, 'recursos': 1, 'reentrada,': 1, 'forçando': 1, 'utilizar': 1, 'lunar': 1,
# 'Aquarius': 1, 'como': 1, 'bote': 1, 'salva-vidas.': 1})

# Encontrando os 5 palavras com mais ocorrencia no texto
print(res.most_common(10))
# [('de', 17), ('a', 7), ('e', 7), ('um', 6), ('do', 5)]
