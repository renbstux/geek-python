"""
Levantando os próprios erros com raise

raise -> Lança Exceções

OBS: O raise não é uma função. É uma palavra resevada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas proprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipodoErro('Mensagem de Erro')

# exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser um string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'Azul')

# exemplo real 2

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser um string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek University', 'preto')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""
# exemplo real

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser um string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek University', 'preto')