"""
Escopo de Variaveis

Dois casos de Escopo:

1- Variaveis Globais;
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa

2- Variaveis Locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variaveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C
int numero = 42;

Exemplo em Java
int numero = 42;

"""
numero = 42
print(numero)
print(type(numero))

numero = 'Renato'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10 # A Variavel 'novo' está declarada localmente dentro do bloco if. portanto, é local
    print(novo)

print(novo)



