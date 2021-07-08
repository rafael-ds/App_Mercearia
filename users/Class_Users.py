import csv


# Objeto usuarios tanto ADM quanto OPR
class Usuario:
    numero_id = 0  # Ao reiniciar o APP o contador volta a posição 1

    def __init__(self, nome, senha, cargo):
        self.__id = Usuario.numero_id + 1
        self.__nome = nome
        self.__senha = senha
        self.__cargo = cargo
        Usuario.numero_id = self.__id

    def nome(self):
        return self.__nome

    def senha(self):
        return self.__senha

    def cargo(self):
        return self.__cargo

    def id(self):
        return self.__id


def salvar_adm(usuario):
    """
    Função que crua um arquivo .csv com os dados do usuario adm.
    OBS: O ID ao reiniciar o APP volta ao numerador 1 --> desenvolver logicar reversa.
    :param usuario:
    """
    with open('s_adm.csv', 'a', newline='', encoding='utf-8') as salvar:
        cabecalho = ['ID', 'NOME', 'CARGO', 'SENHA']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(usuario)


def abrir_adm():
    lista = []

    with open('s_adm.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)

        for i in ler:
            lista.append(i)

        return lista


def atulizar_adm(atl):
    with open('s_adm.csv', 'w', newline='', encoding='utf-8') as atlz:
        cabecalho = ['ID', 'NOME', 'CARGO', 'SENHA']
        escrever = csv.DictWriter(atlz, fieldnames=cabecalho)

        if atlz.tell() == 0:
            escrever.writeheader()

        for i in atl:
            escrever.writerow(
                {'ID': i['ID'], 'NOME': i['NOME'], 'CARGO': i['CARGO'], 'SENHA': i['SENHA']}
            )


def salvar_opr(usuario):
    """
     Função que cria um arquivo .csv com os dados do usuario opr.
    OBS: O ID ao reiniciar o APP volta ao numerador 1 --> desenvolver logicar reversa.

    """
    with open('s_opr.csv', 'a', newline='', encoding='utf-8') as salvar:
        cabecalho = ['ID', 'NOME', 'CARGO', 'SENHA']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(usuario)


def abrir_opr():
    lista = []

    with open('s_opr.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = csv.DictReader(abrir)

        for i in ler:
            lista.append(i)

        return lista
