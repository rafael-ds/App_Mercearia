# ADM -> administradores
# OPR -> Operadores de caixa

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

            if opc == 1:  # Cadastrar

                while True:
                    cadastrar = str(input('Cadastrar novo colaborador? S/N: '))

                    if cadastrar == 's':
                        nome_user = str(input('Informe o nome do colaborador(a): '))
                        senha_user = str(input('Cadestre uma senha do colaborador(a): '))
                        cargo_user = str(input('Informe o cargo do colaborador(a):\n '))

                        #  Instância do Objeto Usuario
                        colaborador = Class_Users.Usuario(nome_user.title(), senha_user, cargo_user)

                        # Condicional para armazenar os dados dos adms
                        if colaborador.cargo() == 'adm':
                            dados_adm = {'ID': colaborador.id(), 'NOME': colaborador.nome(),
                                         'CARGO': colaborador.cargo(), 'SENHA': colaborador.senha()}

                            #  Salva o objeto usuario  .csv do adm
                            Class_Users.salvar_adm(dados_adm)
                            sleep(1)
                            print('Novo ADM cadastrado com sucesso! ')
                            sleep(1)

                        # Condicional para armazenar os dados dos opr
                        elif colaborador.cargo() == 'opr':
                            dados_opr = {'ID': colaborador.id(), 'NOME': colaborador.nome(),
                                         'CARGO': colaborador.cargo(), 'SENHA': colaborador.senha()}

                            #  Salva o objeto usuario  .csv do opr
                            Class_Users.salvar_opr(dados_opr)
                            sleep(1)
                            print('Novo OPR cadastrado com sucesso! ')
                            sleep(1)

                    elif cadastrar == 'n':
                        menu()

            elif opc == 2:  # Alterar
                pass
            elif opc == 3:  # Excluir
                pass
            elif opc == 4:  # Lista de Colaboradores

                opc = int(input('1 - ADM / 2 - OPR: '))

                if opc == 1:
                    print('')
                    Class_Users.abrir_adm()

                    sleep(2)
                    menu()

                elif opc == 2:
                    print('')
                    Class_Users.abrir_opr()

                    sleep(2)
                    menu()

            elif opc == 5:  # Sair
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
