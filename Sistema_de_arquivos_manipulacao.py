"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretorio existe

#Arquivo
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

# Diretorio

#Paths Relativos
print(os.path.exists('geek')) # True
print(os.path.exists('geek/university')) # True
print(os.path.exists('geek/university/geek3.py')) # True
print(os.path.exists('outro')) # false

# Path Absolutos
print(os.path.exists('c:/Users/renbs')) # True
print(os.path.exists('c:/Users/renbs/desktop')) # True


# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close # Cria o arquivo e já fecha

# Forma 2
open('arquivo-teste.txt', 'a').close # Cria o arquivo e já fecha

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

os.mknod('arquivo-teste4.txt')

os.mknod('c:/users/renbs/desktop/university.txt')

# OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError
# OBS: Criando um arquivo via mknod() se o arquivo já  existir teremos o erro FileExistsError

# Criando diretorios

os.mkdir('templates')

# OBS: A função mkdir() cria um diretorio se este não existir. Caso exista, teremos FileExistsError

#OBS: Se não tivermos permissão para criar o diretorio teremos um PermissionError

IMPORTANTE
# Criando Multi-diretorios (arvore de diretorios)
os.makedirs('templates/geek/university')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)


# Renomear arquivos e diretorios

os.rename('geek2', 'Geek2')

#OBS: Se o diretorio não existir teremos um FileNotFoundError

# OBS: Se o diretorio que queremos renomear não estiver vazio, teremos um OSError


# Renomear arquivos e diretorios

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')


# ATENÇAO - Tome cuidado com os comandos de deleção. Ao deletar um arquivo ou diretorio, eles 
# não vão para a LIXEIRA. Eles somem!

os.remove('arquivo-teste3.txt') # Remove Somente Arquivos

#OBS: Se você estiver no windows e o arquivo que você deletar estiver em uso, voce terá um erro.

#OBS: Caso o arquivo não exista, teremos o FileNotFoundError

#OBS: Se você informar um diretorio ao inves de um arquivo, teremos um IsADirectoryError


os.rmdir('templates')

# OBS: Se o diretorio tiver qualquer conteudo teremos OSError

# OBS: Se o diretorio não existir teremos um FileNotFoundError

# Removendo uma arvore de arquivos
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)



# Podemos remover uma arvore de diretorios vazios

os.removedirs('Geek2/mais2/mais4')

# Se algum dos diretorios contiver arquivos ou outros diretorios, o processo para.

Instalar no Windows:
pip install send2trash

Instalar no Linux:

sudo apt-get install lsb-core

pip install send2trash


# Importando a biblioteca send2trash

from send2trash import send2trash

os.remove('outro1.txt') # Não vai para a lixeira. E deletado imediatamente

send2trash('outro.txt') # Vai para lixeira. Pode ser restaurado

"""
import os

# Importando a biblioteca send2trash

from send2trash import send2trash


