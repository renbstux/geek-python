"""
Módulos Customizados

Como módulos Python nada mais são do arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.

# Importando uma função especifica do nosso módulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Importando todo o módulo
import funcoes_com_parametro as fcp

# estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""
from Map import cidades, c_para_f

print(list(map(c_para_f, cidades)))


