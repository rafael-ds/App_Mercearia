# ADM -> administradores
# OPR -> Operadores de caixa
import csv
from time import sleep

from users import Class_Users
from produtos import class_produtos as item

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

        # Caso o arquivo .csv exista
        try:
            print('')
            # Pedido de senha para entrar na configuração de usuario
            senha_acesso = str(input('Informe a senha de acesso: '))

            with open('s_adm.csv', 'r', encoding='utf-8', newline='') as abrir:
                ler = csv.DictReader(abrir)

                # Um filtro que confere se a senha digitada se encontra no arquivo.
                # Cast dos arquivos para lista
                usuario = list(filter(lambda s: s['SENHA'] == senha_acesso, ler))

                if usuario:
                    for i in usuario:
                        user = i.get('NOME')

                    sleep(1)
                    print(f'Usuario Conectado -- {user}')
                    sleep(1)

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

                        # Cadastrar -- OK
                        if opc == 1:

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

                        # Alterar -- OK
                        elif opc == 2:
                            # Lista usada para cast dos dados .csv
                            cast = []

                            opc = int(input('1 - Alterar ADM / 2 - Alterar OPR: '))

                            if opc == 1:
                                # armazenando os itens na variavel dados
                                dados = Class_Users.abrir_adm()

                                # Loop para armazenar os dados no cast
                                for i in dados:
                                    cast.append(i)

                                colab = input('Informe o ID do colaborador(a): ')

                                # Logica de modificação de um item atraves do ID
                                for i in cast:
                                    if i['ID'] == colab:
                                        cast.remove(i)

                                        # Chamada que atualiza os itens do cast para o arquivo .csv
                                        # Sem o item removido
                                        Class_Users.atulizar_adm(cast)

                                        # Criando novos dados:
                                        nome_colab = str(input('Informe o nome do colaborador(a): ')).title()
                                        senha_colab = str(input('Informe a senha do colaborador(a): ')).title()

                                        # Objeto
                                        colaborador = Class_Users.Usuario(nome_colab.title(), senha_colab, cargo='adm')

                                        # Trasformando o OBJ em dicionario
                                        dados_adm = {'ID': colaborador.id(), 'NOME': colaborador.nome(),
                                                     'CARGO': colaborador.cargo(), 'SENHA': colaborador.senha()}

                                        # Escrevendo o dicionario no .csv
                                        Class_Users.salvar_adm(dados_adm)

                                        del cast[:]
                                        sleep(1)
                                        menu()

                                    # Caso o item com ID não seja encontrado
                                    else:
                                        print('Coloborador não encontrado.')
                                        menu()

                            elif opc == 2:
                                dados = Class_Users.abrir_opr()

                                for i in dados:
                                    cast.append(i)

                                colab = input('Informe o ID do(a) colaborador(a): ')

                                for lista in cast:
                                    if lista['ID'] == colab:
                                        cast.remove(i)

                                        # Chamada que atualiza os itens do cast para o arquivo .csv
                                        # Sem o item removido
                                        Class_Users.atulizar_opr(cast)

                                        # Criando novos dados:
                                        nome_colab = str(input('Informe o nome do colaborador(a): ')).title()
                                        senha_colab = str(input('Informe a senha do colaborador(a): ')).title()

                                        # Objeto
                                        colaborador = Class_Users.Usuario(nome_colab.title(), senha_colab, cargo='opr')

                                        # Trasformando o OBJ em dicionario
                                        dados_opr = {'ID': colaborador.id(), 'NOME': colaborador.nome(),
                                                     'CARGO': colaborador.cargo(), 'SENHA': colaborador.senha()}

                                        # Escrevendo o dicionario no .csv
                                        Class_Users.salvar_opr(dados_opr)

                                        del cast[:]
                                        sleep(1)
                                        menu()

                        # Excluir
                        elif opc == 3:
                            cast = []

                            opc = int(input('1 - Excluir ADM / 2 - Excluir OPR: '))

                            if opc == 1:
                                # Armazena os itens .csv na variavel dados
                                dados = Class_Users.abrir_adm()

                                #  For para armazena na lista cast
                                for i in dados:
                                    cast.append(i)

                                colab = input('Informe o ID do(a) ADM: ')

                                for adm in cast:
                                    if adm['ID'] == colab:

                                        del_user = str(input(f"Deseja excluir {adm['NOME']}?\nS/N: "))

                                        if del_user == 's' or del_user == 'S':
                                            sleep(1)
                                            cast.remove(adm)
                                            sleep(1)
                                            # Atualiza o arquivo .csv com os itens restante do cast
                                            Class_Users.atulizar_adm(cast)

                                            sleep(1)
                                            print('Usuario removido com sucesso! ')
                                            sleep(1)

                                            # Limpa a lista cast para não haver problema de repetição de itens
                                            del cast[:]
                                            menu()

                                        elif del_user == 'n' or del_user == 'N':
                                            sleep(1)
                                            del cast[:]
                                            menu()
                                            sleep(1)

                            elif opc == 2:
                                dados = Class_Users.abrir_opr()

                                for i in dados:
                                    cast.append(i)

                                colab = input('Informe o ID do(a) OPR: ')

                                for opr in cast:
                                    if opr['ID'] == colab:

                                        del_opr = str(input(f'Deseja remover {opr["NOME"]}?\nS/N: '))

                                        if del_opr == 's' or del_opr == 'S':
                                            sleep(1)
                                            cast.remove(opr)
                                            sleep(1)
                                            Class_Users.atulizar_opr(cast)
                                            sleep(1)
                                            print('Usuario removido com sucesso! ')

                                            sleep(1)
                                            del cast[:]
                                            menu()

                                        elif del_opr == 'n' or del_opr == 'N':
                                            sleep(1)
                                            del cast[:]
                                            menu()
                                            sleep(1)

                        elif opc == 4:  # Lista de Colaboradores

                            opc = int(input('1 - ADM / 2 - OPR: '))

                            if opc == 1:
                                print('')

                                dados = Class_Users.abrir_adm()
                                for i in dados:
                                    print(i)

                                sleep(2)
                                menu()

                            elif opc == 2:
                                print('')

                                dados = Class_Users.abrir_opr()
                                for i in dados:
                                    print(i)

                                sleep(2)
                                menu()

                        elif opc == 5:  # Sair
                            sleep(1)
                            menu()

                    elif opc == 2:
                        print('=' * 15 + ' Configurações de Produtos ' + '=' * 15 + '\n')

                        print('-' * 60)
                        print(' 1 - Cadastrar / 2 - Alterar / 3 - Excluir / 4 - sair ')
                        print('-' * 60)

                        opc = int(input('Informe a Opção Desejada: '))

                        #  Cadastrar
                        if opc == 1:
                            print('=' * 10 + ' Cadastro de produtos ' + '=' * 10 + '\n')

                            while True:
                                cad = str(input('Cadastrar novo produto? '))

                                if cad == 's' or cad == 'S':

                                    try:
                                        codigo_prod = int(input('Informe o codigo do produto: '))
                                    except ValueError:
                                        print('É necessario inserir o codigo do produto: ')
                                        codigo_prod = int(input('Informe o codigo do produto: '))

                                    nome_produto = str(input('Informe o nome do produto: ')).title()
                                    descricao_prod = str(input('Informe a descricao do produto: '))

                                    try:
                                        valor_prod = float(input('Informe o valor do produto: '))
                                    except ValueError:
                                        print('É necessario inserir o valor do produto: ')
                                        valor_prod = float(input('Informe o valor do produto: '))

                                    produto = item.Produtos(codigo_prod, nome_produto, descricao_prod, valor_prod)

                                    prd = {'COD': produto.codigo(), 'PRODUTO': produto.nome(),
                                           'DESCRIÇÃO': produto.descricao(), 'VALOR(R$)': produto.valor()}

                                    sleep(.5)
                                    item.cadastrar_prod(prd)

                                elif cad == 'n' or cad == 'N':
                                    sleep(1)
                                    menu()

                        # Alterar
                        elif opc == 2:
                            cast = []

                            print('=' * 10 + ' Alterar produtos ' + '=' * 10 + '\n')

                            #  Armazenamento da função lista_prod()
                            prod = item.lista_prod()

                            #  for para add. os intens da lista no cast
                            for i in prod:
                                cast.append(i)

                            #  Estetica, só para mostrar os itens
                            for itens in cast:
                                print(itens)

                            sleep(1)

                            cod = input('Informe o codigo do produto a ser alterado: ')

                            for produto in cast:
                                if produto['COD'] == cod:
                                    # Mostra somente o produto do codigo
                                    print(produto)

                                    while True:
                                        opc = str(input('Alterar Produtos? S/N'))

                                        if opc == 's' or opc == 'S':
                                            alterar = int(input('Alterar -- 1 - COD / 2 - Produtos / 3 - Descrição / 4 - '
                                                                'Valor(R$) '))

                                            # Alterar o codigo do produto
                                            if alterar == 1:
                                                novo_cod = int(input('Informe o codigo para o produto: '))
                                                produto.update({'COD': novo_cod})

                                                sleep(.5)
                                                print('Codigo alterando com sucesso')
                                                # -----------continue --------------------
                                        elif opc == 'n' or opc == 'N':
                                            sleep(1)
                                            menu()

                            print(prod)
                            sleep(.5)
                            menu()
                        elif opc == 3:
                            pass
                        elif opc == 4:
                            menu()

                    elif opc == 3:
                        pass
                    elif opc == 4:
                        sleep(1)
                        menu()
                else:
                    print('Senha invalida! ')
                    menu()

        # Cria um arquivo .csv caso não exista
        except FileNotFoundError:
            print('É Necessário Cadastrar Um Administrador! ')

            cadastrar = str(input('Cadastrar um Administrador? S/N: '))

            if cadastrar == 's':
                nome_user = str(input('Informe o nome do colaborador(a): '))
                senha_user = str(input('Cadestre uma senha do colaborador(a): '))

                # Instancia do objeto usuario com caracteristica de adm
                adm = Class_Users.Usuario(nome_user.title(), senha_user, 'adm')

                # Dicionadio para salvar no .csv
                save_dados = {'ID': adm.id(), 'NOME': adm.nome(),
                              'CARGO': adm.cargo(), 'SENHA': adm.senha()}

                # Salva o objeto convertido em dict em .csv
                Class_Users.salvar_adm(save_dados)
                sleep(1)
                print('Administrador cadastrado com sucesso! ')
                sleep(1)

                menu()

            elif cadastrar == 'n':
                menu()

    elif opc == 4:
        menu()
    elif opc == 5:
        pass

    print('-' * 60)


menu()
