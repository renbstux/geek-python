import collections
from timeit import timeit

Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

print(timeit('felicity.email', globals=globals()))

print(globals())

import sys

print(sys.getsizeof(list(range(29082020))))