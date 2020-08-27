"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - Sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. CASO O ARQ EXISTA, GERA FileExistsError.
a -> Abre para escrita. Adicionando o conteudo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita.

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteudo sera
adicionado ao final do arquivo SEMPRE. Com o modo 'a', não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2.\n')
except FileExistsError:
    print('Arquivo já existe')


with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break



#Exemplo r+
with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Outro No topo!\n')
    arquivo.seek(32)
    arquivo.write('Nova Linha.\n')
    arquivo.seek(20)
    arquivo.write('Mais uma linha.\n')
"""

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
