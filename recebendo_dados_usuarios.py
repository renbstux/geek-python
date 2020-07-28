"""

Recebendo dados do usuario

input() => Todo dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas Duplas;
- Aspas Simples Triplas;
- Aspos Duplas Triplas;

Exemplos:
- Aspas Simples -> 'Angelina Jolie'
- Aspas Duplas -> "Angelina Jolie"
- Aspas Simples Triplas -> '''Angelina Jolie'''
- Aspas Duplas Triplas ->
"""
# Entrada de dados
#print("Qual o seu nome?")
#nome = input()

nome = input('Qual o Seu Nome? ') # Entrada de dados

# Exemplo de Print 'antigo' 2.x Python
#print('Seja Bem-Vindo(a) %s' % nome)

#Exemplo de print moderno criado versões 3 do Python
#print('Seja Bem vindo(a) {0}'.format(nome))

#Exemplo de print mais 'mais atual' 3.7 >
print(f'Seja bem vindo(a) {nome}')

#print("Qual a sua Idade:")
# idade = input()

#idade = input('Qual a sua idade: ')
idade = int(input('Qual a sua idade: ')) # Se entrada necessita de um numero int, ja informe na entrada da Variavel

# Processamento

# Saida de Dados
# Exemplo de Print 'antigo' 2.x Python
#print('O(A) %s tem %s anos' % (nome, idade))

#Exemplo de print moderno criado versões 3 do Python
#print('O {0} tem {1} anos'.format(nome, idade))

#Exemplo de print mais 'mais atual' 3.7 >
print(f'O {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
#print(f'O {nome} nasceu em {2020 - int(idade)}')
print(f'O {nome} nasceu em {2020 - idade}')