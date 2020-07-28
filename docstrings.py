"""
Documentando funções com DocStrings

print(help(print))

OBS: Podemos ter acesso a documentação de uma funçãoe em Python
utilizando a propriedade especial __doc__

print.__doc__
help.__doc__

Podemos ainda fazer acesso a documentação com a função help()
"""
# Exemplo

def diz_oi():
    """Uma função simples que retorna a string OI! """
    return 'Oi!'

print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: |Numero que desejamos gerar o exponencial
    :param potencia: |Potencia que queremos gerar o exponencial. Por padrão é 2.
    :return: |Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia

print(help(exponencial))