"""
Assertions (Afirmações) seria mais (Checagens/Questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None é caso seja falsa levanta um erro
do tipo AssertionError.

#Obs: nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada.

#OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso...não precisa
ser exclusivamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um Programa Python for executado com parametro -O, nenhum assertion
será validado. Ou seja, todas as suas validações já eram.



"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > a, 'Ambos numeros precisam ser positivos'
    return a + b

ret = soma_numeros_positivos(2, 4)#  6
#ret = soma_numeros_positivos(-2, 4)#  AssertionError: Ambos numeros precisam ser positivos
#print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita'
        'cachorro quente',
    ], 'A comida precisa ser fast food!'
    return f'Eu estou comendo {comida}'

comida = input('informe a comida: ')
print(comer_fast_food(comida))





