"""
Tipo Booleano

Algebra Booleana, criada por George Boole

True -> Verdadeiro
False -> Falso

Obs: Sempre com inicial em maiuscula

Errado:

true, false

Certo:

True, False

"""
ativo = True

print(ativo)
"""
Operações Basicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso.
Se for falso o resultado será verdadeiro. Ou seja sempre ao contrario.
"""
print(not ativo)

logado = False
# Ou (or)
"""
É uma operação binaria, ou seja, depende de dois valores, Ou seja, ou um outro deve ser verdadeiros

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print (ativo or logado)

# E (and)
"""
Também é uma operação binaria, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False

>>> 5 > 6
False
>>> 5 < 6
True
>>> 6 == 6
True
>>> 4 <= 5
True

>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> ativo = True
>>> type(ativo)
<class 'bool'>
>>> dir(ativo)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '_
_floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_sub
class__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__
pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '
__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__
sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'ima
g', 'numerator', 'real', 'to_bytes']

"""
