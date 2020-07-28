"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa Função
retorna _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos
o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>

mode='r' -> Modo de Leitura. r-> read()

"""

# Exemplo

arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

#print(arquivo.read())

# obs: o PYthon, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse Cursor,
# Funciona como o cursor quando estamos escrevendo.

#print(arquivo.read())

# OBS: A função read() lê todo o conteúdo do arquivo.

