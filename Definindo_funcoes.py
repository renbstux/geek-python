"""
Definindo Funções

- Funções são pequenas partes de códigos que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornas uma saida de dados;
- Muito uteis para executar procedimento similares repetidas vezes;

Obs: Se você escrever uma função que realiza varias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada

Já utilizamos varias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""
# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do Python print()

#print(cores)

#curso = 'Programação em Python: Essencial'

#print(curso)

#cores.append('roxo')
#print(cores)

#cores.clear()
#print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita o seu código

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir um função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgulas, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

Obs.: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma função. Também abrimos o bloco de codigo com o já conhecido dois pontos : que é Utilizado em Python para definir 
blocos.
"""

# definindo a primeira função
# Definição
def diz_oi():
    print('oi!')

"""
OBS.: 

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que está função não recebe nenhum parametro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando funções
# Chamada de execução
#diz_oi()
"""
ATENÇÃO 

Nunca esquece de utilizar o parenteses () ao executar um função.

Exemplo:

#ERRADO!
diz_oi

#CERTO!
diz_oi()
"""

def cantar_parabens():
    print('Parabens para você')
    print('Nesta dara querida')
    print('Muitas felicidades')
    print('Muitos Anos de vida')
    print('Viva o Aniversariante!')

#for n in range(5):
#   cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma função e executar esta função atraves da variavel

canta = cantar_parabens

canta()