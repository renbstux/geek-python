"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do 
modulo OS

os -> Operating Sitem - Sistema Operacional

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretorio de trabalho corrente
print(os.getcwd())

# Para mudar o diretorio, podemos utilizar o chdir()    

os.chdir('..')

print(os.getcwd())


#Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('c:/Users/renbs'))

# Podemos identificar o sistema operacional com o modulo os

print(os.name) # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional

print(os.uname()) # Linux

print(sys.platform)
"""

"""
print(os.getcwd()) # C:\\Users\\renbs\\PycharmProjects\\renbstux

res = os.path.join(os.getcwd(), 'geek', 'University')

os.chdir(res) # C:\\Users\\renbs\\PycharmProjects\\renbstux\\geek\\University

#Veja que o os.path.join() recebe dois parametros, sendo o primeiro o diretorio atual e o segundo o
#diretorio que será juntado ao atual.

print(os.getcwd())

"""


# Fazer o import
import os

# Podemos listar os arquivos e diretorios com o listdir()


scanner = os.scandir()

arquivos = list(scanner)

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # E um diretorio? False
print(arquivos[0].is_file()) # E um arquivo? True
print(arquivos[0].is_symlink()) # E um link simbolico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # ???

# Obs: Quando utilizamos a função scandir() nos precisamos fecha-la, assim quando abrimos um arquivo.

scanner.close()