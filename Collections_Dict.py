"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html?highlight=collections#collections.defaultdict

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])
print(dicionario['outro'])  # ??? KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default será
atribuido.
"""

# Fazendo Import

from collections import defaultdict

dicionario = defaultdict(lambda: 1)

print(type(dicionario))

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionario comum, mas aqui não.

print(dicionario)
