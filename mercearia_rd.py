# ADM -> administradores
# OPR -> Operadores de caixa
import csv
from time import sleep

from users import Class_Users
from produtos import class_produtos as item
from clientes import class_clientes as bd_clientes

sleep(1)


def menu():
    print('')
    print('=' * 25 + ' Mercadinho ' + '=' * 25)
    print('1 - Iniciar Caixa\n'
          '2 - Conferir Produtos\n'
          '3 - Configurações\n'
          '4 - Sair\n')

    opc = int(input('Informe a opção desejada: '))

    # Iniciar Caixa
    if opc == 1:
        try:
            print('=' * 15 + ' Caixa ' + '=' * 15 + '\n')
            print('')
            senha_acesso = input('Informe a sua senha de acesso: ')

            acesso = Class_Users.abrir_opr()
            user_opr = list(filter(lambda u: u['SENHA'] == senha_acesso, acesso))

            def menu_caixa():
                """
                Função Interna que tem como objetivo a opreração do caixa
                Passagem de produtos
                Balanço do caixa
                Fechamento do caixa
                Retorno ao menu principal

                """
                lista_itens = []
                cod = ''

                for opr in user_opr:
                    sleep(1)
                    print(f"Caixa aberto - OPR: {opr.get('NOME')}\n")

                print('1 - Passar produto\n'
                      '2 - Balaço do caixa\n'
                      '3 - Cadastro clientes\n'
                      '4 - Fechar caixa\n'
                      '5 - Menu pricipal\n ')

                opc = int(input('Informe a opção desejada: '))

                # Passar produtos
                if opc == 1:
                    # chamada global para iterar na condicional club
                    global total

                    # Menu para passar os produtos
                    while cod != 's':
                        cod = input('Codigo do produto: ')
                        print('')

                        bd_prod = item.lista_prod()
                        itens = list(filter(lambda i: i['COD'] == cod, bd_prod))

                        if itens:

                            # loop para manipulação dos itens add na lista itens
                            # loop de estetica
                            for i in itens:
                                lista_itens.append(i.get('VALOR(R$)'))

                                print(f"Cod: {i.get('COD')}")
                                print(f"Produto: {i.get('PRODUTO')}")
                                print(f"Descrição: {i.get('DESCRIÇÃO')}")
                                print(f"Preço: R${i.get('VALOR(R$)')}")
                                print('-' * 60)
                                print('')

                            # list comprehension para iterar sobre
                            # os itens da lista_itens
                            # OBS: variavel com chamada global
                            total = [float(i) for i in lista_itens]

                            print('-' * 30)
                            print(f'Total - R${sum(total):.2f}')
                            print('-' * 30)

                    club = input('Club? S/N: ')

                    # Condicional que verifica se o cliente tem seu cpf cadastrado para
                    # para descontos
                    if club == 's' or club == 'S':

                        enter_cpf = input('Informe o CPF: ')

                        lista_cliente = bd_clientes.lista_clientes()
                        buscar_cliente = list(filter(lambda b: b['CPF'] == enter_cpf, lista_cliente))

                        if buscar_cliente:
                            for nome in buscar_cliente:
                                print(f'Seja bem vindo(a) {nome.get("NOME")}\n')

                            desconto = 10  # 10%
                            total_desc = sum(total) * desconto / 100
                            total_pg = sum(total) - total_desc

                            print('-' * 50)
                            print(f'Valor desconto: R${total_desc:.2f}')
                            print(f'Valor Total: R${total_pg:.2f}')
                            print('-' * 50)

                            valor_recebido = float(input('Valor recebido: '))
                            troco = valor_recebido - total_pg
                            print(f'Troco = R${troco:.2f}\n')
                            print('-' * 50)

                            sleep(1)
                            menu_caixa()

                        else:
                            # ------------
                            # Criar Logica para permanencia dos valores
                            # Caso o o cpf não esteja cadastrado
                            # ----------------
                            print('Usuario nao cadastrado!\n')
                            menu_caixa()

                    elif club == 'n' or 'N':

                        print('-' * 50)
                        print(f'Valor apagar: R${sum(total)}')
                        valor_recebido = float(input('Valor recebido: '))
                        troco = valor_recebido - sum(total)

                        print(f'Troco = R${troco:.2f}\n')

                        sleep(1)
                        menu_caixa()

                # Balanço do caixa
                elif opc == 2:
                    pass

                elif opc == 3:
                    # Cadastrar Clientes
                    print('-' * 50 + ' Cadastrar cliente ' + '-' * 50)

                    nome = str(input('Nome do cliente: ')).title()
                    tel = int(input('Telefone: '))
                    email = str(input('E-mail: '))
                    cpf = int(input('CPF: '))

                    cliente = bd_clientes.Clientes(nome, tel, email, cpf)
                    dados_cliente = {'NOME': cliente.nome(), 'TEL.': cliente.telefone(),
                                     'EMAIL': cliente.email(), 'CPF': cliente.cpf()}

                    bd_clientes.cad_cliente(dados_cliente)
                    print('Cliente cadastrado com sucesso.\n')
                    sleep(1)

                    menu_caixa()

                # Fechar caixa
                elif opc == 4:
                    pass

                # Menu principal
                elif opc == 5:
                    sleep(1)
                    menu()

            # Condicional que verifica a existencia do operador de caixa
            if user_opr:
                sleep(1)
                menu_caixa()

            else:
                sleep(.5)
                print('Usuario não encontrado! ')
                sleep(.5)
                menu()

        except FileNotFoundError:
            pass

    # Conferir Produtos
    elif opc == 2:
        menu()

    # Configurações
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

                    # Config. do Colaboradores
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

                        # Lista de Colaboradores
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

                        # Sair
                        elif opc == 5:  #
                            sleep(1)
                            menu()

                    # Config. de  Produtos
                    elif opc == 2:
                        cast = []

                        print('=' * 30 + ' Configurações de Produtos ' + '=' * 30 + '\n')

                        print('-' * 75)
                        print(' 1 - Cadastrar / 2 - Alterar / 3 - Excluir / 4 - Listagem de produtos / 5 - sair ')
                        print('-' * 75)

                        opc = int(input('Informe a Opção Desejada: '))

                        #  Cadastrar
                        if opc == 1:
                            print('=' * 10 + ' Cadastro de produtos ' + '=' * 10 + '\n')

                            while True:
                                cad = str(input('Cadastrar novo produto?\nS/N: '))

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

                                    print('-' * 50 + '\n')

                                elif cad == 'n' or cad == 'N':
                                    sleep(1)
                                    menu()

                        # Alterar
                        elif opc == 2:

                            print('=' * 10 + ' Alterar produtos ' + '=' * 10 + '\n')

                            #  Armazenamento da função lista_prod()
                            prod = item.lista_prod()

                            #  for para add. os intens da lista no cast
                            for i in prod:
                                cast.append(i)

                            #  Estetica, só para mostrar os itens
                            print('-' * 30 + ' LISTA DE PRODUTOS ' + '-' * 30)
                            for itens in cast:
                                print(itens)
                            print('-' * 90)
                            sleep(1)

                            while True:
                                opc = str(input('Fazer alteração do produto?\nS/N: '))

                                if opc == 's' or opc == 'S':
                                    cod = input('Informe o codigo do produto a ser alterado: ')
                                    print('')
                                    for produto in cast:
                                        if produto['COD'] == cod:
                                            sleep(.3)
                                            print(produto)
                                            print('')

                                            alterar = int(input(
                                                'Alterar -- 1 - COD / 2 - Produtos / 3 - Descrição / 4 - Valor(R$) '))

                                            if alterar == 1:
                                                novo_cod = int(input('Informe o codigo para o produto: '))
                                                produto.update({'COD': novo_cod})

                                                sleep(.5)
                                                print('Codigo do produto alterando com sucesso.\n')

                                            # Alterar o nome do produto
                                            elif alterar == 2:
                                                novo_prod = str(input('Informe o nome do produto: ')).title()
                                                produto.update({'PRODUTO': novo_prod})

                                                sleep(.5)
                                                print('Nome do produto alterando com sucesso.\n')

                                            elif alterar == 3:
                                                novo_desc = str(input('Informe a descrição do produto: '))
                                                produto.update({'DESCRIÇÃO': novo_desc})

                                                sleep(.5)
                                                print('Descrição do produto alterando com sucesso.\n')

                                            elif alterar == 4:
                                                novo_preco = float(input('Informe o valor do produto: '))
                                                produto.update({'VALOR(R$)': novo_preco})

                                                sleep(.5)
                                                print('Preço do produto alterando com sucesso.\n')

                                # --- Comparação ocorrendo erro de buscas --- #
                                # elif produto['COD'] != cod:
                                #     print('Código não encontrado.')
                                elif opc == 'n' or opc == 'N':
                                    item.atualizar_lista(cast)
                                    sleep(.5)
                                    del cast[:]
                                    sleep(1)
                                    menu()
                            #
                            # print(prod)
                            # sleep(.5)
                            # menu()

                        elif opc == 3:
                            print('=' * 10 + ' Excluir Produtos ' + '=' * 10 + '\n')

                            lista_pdt = item.lista_prod()

                            for produtos in lista_pdt:
                                cast.append(produtos)

                            while True:
                                opc = input('Excluir produtos:\nS/N: ')

                                if opc == 's' or opc == 'S':
                                    cod = input('Informe o codigo do produto: ')
                                    sleep(.5)

                                    produto = list(filter(lambda p: p['COD'] == cod, cast))

                                    if produto:
                                        # for de estetica. mostra o produto pedido na integra
                                        for pdt in produto:
                                            print('-' * 50)
                                            print(f'Cod: {pdt["COD"]}')
                                            print(f'Produto: {pdt["PRODUTO"]}')
                                            print(f'Descrição: {pdt["DESCRIÇÃO"]}')
                                            print(f'Preço: {pdt["VALOR(R$)"]}')
                                            print('-' * 50)

                                            exc = input(f'Excluir produto -- {pdt["PRODUTO"]}?\nS/N: ')

                                            if exc == 's' or exc == 'S':
                                                cast.remove(pdt)
                                                sleep(1)
                                                item.atualizar_lista(cast)
                                                sleep(.5)
                                                del cast[:]
                                                print('Produto excluido com sucesso!\n')

                                    else:
                                        print('Codigo não encontrado.\n')

                                elif opc == 'n' or opc == 'N':
                                    sleep(.5)
                                    menu()

                        # Listagem de Produtos
                        elif opc == 4:
                            print('=' * 20 + ' Listagem de Produtos ' + '-' * 20 + '\n')
                            pdt = item.lista_prod()

                            for produtos in pdt:
                                sleep(.5)
                                print('-' * 50)
                                print(f"Cod: {produtos['COD']}")
                                print(f"Produto: {produtos['PRODUTO']}")
                                print(f"Descrição: {produtos['DESCRIÇÃO']}")
                                print(f"Preço: {produtos['VALOR(R$)']}")

                            menu()

                        # Sair
                        elif opc == 5:
                            menu()

                    # Config. de  Vendas
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

    # Sair
    elif opc == 4:
        exit(0)

    print('-' * 60)


menu()
