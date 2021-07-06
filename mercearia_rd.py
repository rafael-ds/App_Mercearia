from users import Class_Users

from time import sleep

users_adm = []
users_opr = []
lista_users = []

sleep(1)


def menu():
    print('')
    print('=' * 25 + ' Mercadinho ' + '=' * 25)
    print('1 - Iniciar Caixa\n '
          '2 - Passar Produtos\n '
          '3 - Configurações\n '
          '4 - Cadastrar Clientes\n '
          '5 - Fechar Caixa\n ')

    opc = int(input('Informe a opção desejada: '))

    if opc == 1:
        menu()
    elif opc == 2:
        menu()

    elif opc == 3:
        print('')
        print('=' * 15 + ' Configurações do Sistama ' + '=' * 15 + '\n')

        print(' 1 - Config. do Colaboradores:\n '
              '2 - Config. de  Produtos:\n '
              '3 - Config. de  Vendas:\n '
              '4 - Sair:\n ')

        opc = int(input('Informe a Opção Desejada: '))

        if opc == 1:
            print('-' * 60)
            print(' 1 - Cadastrar / 2 - Alterar / 3 - Excluir / 4 - Lista de Colaboradores / 5 - sair ')
            print('-' * 60)

            opc = int(input('Informe a Opção Desejada: '))

            # Refatorar para um sistema de repetição a ter o cancelamento
            if opc == 1:
                cadastrar = str(input('Cadastrar novo colaborador? S/N: '))

                if cadastrar == 's':
                    nome_user = str(input('Informe o nome do colaborador(a): '))
                    senha_user = str(input('Cadestre uma senha do colaborador(a): '))
                    cargo_user = str(input('Informe o cargo do colaborador(a):\n '))

                    colaborador = Class_Users.Usuario(nome_user.title(), senha_user, cargo_user)

                    if colaborador.cargo() == 'adm':
                        users_adm.append(colaborador)

                    elif colaborador.cargo() == 'opr':
                        users_opr.append(colaborador)

                elif cadastrar == 'n':
                    menu()
            # ---------------------------------------------------------------
            elif opc == 2:
                pass
            elif opc == 3:
                pass
            elif opc == 4:

                opc = int(input('1 - ADM / 2 - OPR: '))

                if opc == 1:
                    print('')
                    for lista in users_adm:
                        print(f'ID: {lista.id()} - '
                              f'Colaborardor: {lista.nome()} - '
                              f'Cargo {lista.cargo()}')
                    # menu()

                elif opc == 2:
                    print('')
                    for lista in users_opr:
                        print(f'ID: {lista.id()} - '
                              f'Colaborardor: {lista.nome()} - '
                              f'Cargo {lista.cargo()}')
                    # menu()

            elif opc == 5:
                sleep(1)
                menu()

        elif opc == 2:
            pass
        elif opc == 3:
            pass
        elif opc == 4:
            sleep(1)
            menu()

    elif opc == 4:
        menu()
    elif opc == 5:
        pass

    print('-' * 60)


menu()
