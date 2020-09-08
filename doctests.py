"""
Doctests

Doctests são testes que colocamos na docstring das funções/metodos Python

python -m doctest -v nome_do_modulo.py

def soma(a, b):
    # soma os numeros a e b

    #>>> soma(1, 2)
    #3

    #>>> soma(4, 6)
    #10

    return a + b

Saída:
7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

________________________________________________________________

# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    Duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c'])
    #['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #   ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    return [2 * elemento for elemento in valores]

__________________________________________________________________
# Erro inesperado...

Obs.: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

def fala_oi():
    # Fala oi

    #>>> fala_oi()
    #'oi'

    return "oi"
"""
# Um ultimo caso estranho...

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
