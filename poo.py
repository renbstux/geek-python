"""
Programação Orientada a Objetos - POO

 - POO é uma paradigma de programação que utiliza mapeamento
de objetos do mundo real para modelos computacionais.

 - Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

 Principais elementos de Orientação a Objetos
  - Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
  - Atributo -> Caracteristicas do Objeto.
  - Metodo -> Comportamento do objeto (funções).
  - Construtor -> Método especial utilizado para criar os objetos;
  - Objeto -> Instancia da Classe.
"""

numero = 10

print(numero)
print(type(numero))

nome = 'Geek'
print(nome)
print(type(nome))


class Produto:
    pass

ps4 = Produto() # Construtor Padrão e o ps4 é o Objeto
print(ps4)
print(type(ps4))

