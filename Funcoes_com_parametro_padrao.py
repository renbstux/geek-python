"""
Funções com Parametros padrão (Default Parameters)

- Funções onde a passagem de parametro seja opcional;

# Exemplo de função onde a passagem de parametro seja opcional

print('Geek University')

print()

# Exemplo de função onde a passagem de parametro seja obrigatoria

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # Type ERROR

def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 + 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3))# Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva a potencia informada pelo usuario

# OBS
# Se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero, e sera calculado o quadrado
# desre numero;
# Se o usuario passar 2 argumentos, o primeiro será atribuido ao parametro numero e o segundo ao parametro potencia.
# Então será calculada esta potencia.

#OBS: Em função Python, os parametros com valores default(padrão) DEVEM sempre estar ao final da declaração.

#ERRO!
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# Outros Exemplos
def soma(num1=0, num2=0):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  #TypeError
print(soma())   #TypeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo Instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o Instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao('Renato'))
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome='Melissa'))

# por quê utilizar parametros com valor default?

- Nos permite ser mais flexiveis nas funçoes;
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de codigo

# Quais tipos de dados podemos utilizar como valores default para paremetros?

- Qualquer tipo de dados:
    - Numeros, Strings, floats, booleans, listas, tuplas, dicionarios, funções e etc;

def diz_oi():
    print('oi')

variavel = diz_oi

variavel()


#Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variaveis globais
# Variaveis locais

instrutor = 'Geek' # variavel global

def diz_oi():
    instrutor = 'Python' # Variavel local
    return f'Oi {instrutor}'

print(diz_oi())

#OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local terá preferencia.

def diz_oi():
    prof = 'Geek' # Variavel local
    return  f'Ola {prof}'

print(diz_oi())

print(prof)# NameError

# ATENÇÂO com variaveis globais (se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 #UnboundLocalError (A Variavel local esta sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variavel global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""
# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador # Essa variavel não local, como ela tb não é global e que esta na funçao anterior
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
