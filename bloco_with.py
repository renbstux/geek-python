"""
O Bloco With

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

o bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados
apos o bloco with.

"""

# o bloco with - Forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

#print(arquivo.read())

print(arquivo.closed)
