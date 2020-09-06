"""
Por que testar nosso codigo?

Testes Automatizados!


                       Aplicação Web
------------------------------------------------------------
|                                                          |
|                Frontend e Backend                        |
------------------------------------------------------------
|                 Testes Automatizados                     |
------------------------------------------------------------

Por que testar nosso codigo?
    - Reduzir Bugs , problemas no código existe;
    - Testes garantem que novos recursos da sua aplicação não quebrem(alterem) recursos antigos;
    - Testes garantem que bugs(problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refataroção que costumamos a fazer não tragam novos bugs!;

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estagios de desenvolvimento:
    - Você escreve seu teste primeiro:
    - Então você escreve o código minimo suficiente para fazer o teste passar(ou seja, executar com sucesso);
    - Então refatora o codigo para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Esses estagios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;
"""

class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')

felix.miar()

print(felix.nome)