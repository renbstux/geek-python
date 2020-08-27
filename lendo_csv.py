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

"""
with open('lutadores.csv') as file:
    dados = file.read()
    dados = dados.split(',')[2:]
    print(file)
