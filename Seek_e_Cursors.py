"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> a função seek é utilizada para movimentação do cursor pelo arquivo. Ela recebe um
# paramentro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com a função seek() -. Procurar

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())


arquivo = open('texto.txt')

# readline() função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))


# readlines()

linhas = arquivo.readlines()

print(arquivo.readlines())

print(len(linhas))


# OBS: Quando abrimos um arquivo com a funçao open() é criada uma conexão entre o arquivo no disco do
computador e o nosso programa. Essa conexao é chamada de streaming.
Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o Arquivo;

3 - Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o Arquivo;
print(arquivo.read())

print(arquivo.closed)      # Verifica se o arquivo aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed)      # Verifica se o arquivo aberto ou fechado

# OBS: Se tentarmos manipular o arquivo apos o deu fechamento , teremos um ValueError
"""
arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))
