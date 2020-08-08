"""
Decoradores (Decorators)

O que são Decorators?

 - Decorators são funções;
 - Decorators envolvem outras funções e aprimoram seus comportamentos;
 - Decorators também são exemplos de High Order Functions;
 - Decorators tem uma sintaxe própria, usando "@" (Suntact Sugar / Açucar Sintático)


 |-----------------------------------------------------|
 |               Function Decorator                    |
 |-----------------------------------------------------|

 ------------------------------------------------------
 |-----------------------------------------------------|
 | |                    Function                     | | 
 |-----------------------------------------------------|
 -------------------------------------------------------

 # Decorators como funções (Sintaxe não recomendada / Sem Açucar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja Bem-vindo(a) a Geek University')

# Testando 1

#saudacao()

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorator com Sintax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao): # Essa é a função Decoradora ou Decorator Function
    def sendo_mesmo():
        print('Foi um prazer conhecer você?')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

@seja_educado_mesmo # Isso é um Decorator
def dormir():
    print('Quero dormir...')

dormir()

"""
# OBS: Não confunda Decorator com Decorator Function

