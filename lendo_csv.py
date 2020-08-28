"""
Lendo Arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula

1, 2, 3, 4, 5, 6

geek, university, python, ciencia, dados

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

geek; university; python; ciencia; dados

# Separador por espaço

1  2  3  4  5  6

geek university python ciencia  dados

http://dados.gov.br/dataset

# Possivel de se trabalhar, mas não é o ideal (trabalhoso)

with open('lutadores.csv') as file:
    dados = file.read()
    dados = dados.split(',')[2:]
    print(file)

A linguagem Python duas formas diferente para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    -DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;


# Reader

from csv import reader

with open('lutadores.csv', encoding='UTF8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no {linha[1]} e mede {linha[2]} centimetros')



# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='UTF8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
"""

# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv', encoding='UTF8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

