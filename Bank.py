"""
Descrição:
Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o
que deseja fazer no banco, como criar uma conta, efetuar saque, efetuar depósito, efetuar
transferência, listar contas ou sair do sistema

Description:
We must develop an application where, when initialized, ask the user to choose the
you want to do at the bank, how to create an account, make a withdrawal, make a deposit, make
transfer, list accounts or log out
"""

from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()


def menu() -> None:
    print('========================================================================')
    print('============================= A T M ====================================')
    print('======================= G E E K  B A N K ===============================')
    print('========================================================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Depósito')
    print('4 - Efetuar Transferência')
    print('5 - Listar Contas')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(5)
        exit(0)
    else:
        print('Opção Inválida')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do Cliente: ')
    email: str = input('E-mail do Cliente: ')
    cpf: str = input('Informe o CPF do Cliente:')
    data_nascimento: str = input('Informe a data do nascimento XX/XX/XXXX:')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('_________________________________________')
    print(conta)
    sleep(2)
    menu()




def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta para depósito: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Não foi encontrada um conta com numero {numero}')
    else:
        print('Ainda não exsitem contas cadastradas!')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o numero da sua conta: '))

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe o numero da conta de destino: '))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor de transferência: '))

                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A conta destino com numero {numero_destino} não foi encontrada!')
        else:
            print(f'A Sua Conta com numero {numero_origem} não foi encontrada!')

    else:
        print('Ainda não existem contas cadastradas!')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('__________________________________________________________________')
            sleep(1)

    else:
        print('Não existem conta cadastradas!')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()

