"""
Tipo String

Já vimos que em Python um dado é considerado do tipo string sempre que:

Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'

Estiver entre aspas Duplas -> "uma string", "234", "a", "True", "42.3"

Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre aspas Duplas Triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

"""
nome = 'Renato de Souza'
print(nome)
print(type(nome))

nome = "Renato's Bar"
print(nome)
print(type(nome))

nome = "Melissa \nLuz"  # \n e como se desse um enter para separar a linha
print(nome)
print(type(nome))

nome = ""Melissa
Luz""
print(nome)
print(type(nome))

nome = 'Renato de Souza'
print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em lista de Strings - 
['Renato', 'de', 'Souza'] 

print(nome[0:6]) # Slice de String

print(nome[7:15]) # Slice de String

print(nome.split()[0])

print(nome.split()[2])
"""
# [  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,   14 ]
# [ 'R', 'e', 'n', 'a', 't', 'o', ' ', 'd', 'e', ' ', 'S', 'o', 'u', 'z', 'a' ]
nome = 'Renato de Souza'
"""
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento e inverta

azuoS ed otaneR

print(nome[::-1]) # Pythônico -> Inversão da String

print(nome.replace('a', '@'))

Ren@to de Souz@
"""
print(nome[::-1]) # Pythônico -> Inversão da String

print(nome.replace('a', '@'))

texto = 'socorram me subino onibus em marrocos' # Palindromo
print(texto)

print(texto[::-1])





