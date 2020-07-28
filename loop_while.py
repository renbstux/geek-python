"""
Loop While

Forma Geral

while expressão Booleana:
    //execução do loop

O bloco do while será repetida enquanto a expressão booleana for verdadeiro.

expressão booleana é toda expressão onde o resultado for verdadeiro ou falso!

exemplo:

num = 5

num < 5
False

# Exemplo 1
numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: em um loop while que cuidemos do criterio de parada para não causar loop infinito.



"""
# Exemplo 2

resposta = ''

while resposta != 'sim': # != => Diferente
    resposta = input('Já acabou Jéssica? ')
