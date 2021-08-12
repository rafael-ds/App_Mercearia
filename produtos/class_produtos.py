import csv
from data_hora import data_hora as dh


class Produtos:
    def __init__(self, codigo, nome, descricao, valor):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def codigo(self):
        return self.__codigo

    def nome(self):
        return self.__nome

    def descricao(self):
        return self.__descricao

    def valor(self):
        return self.__valor


def cadastrar_prod(produto):
    with open('produtos.csv', 'a', encoding='utf-8', newline='') as salvar:
        cabecalho = ['COD', 'PRODUTO', 'DESCRIÇÃO', 'VALOR(R$)']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(produto)


def lista_prod():
    lista = []

    with open('produtos.csv', 'r', encoding='utf-8', newline='') as abrir:
        ler = csv.DictReader(abrir)

        for i in ler:
            lista.append(i)

    return lista


def atualizar_lista(atz):
    with open('produtos.csv', 'w', newline='', encoding='utf-8') as atlz:
        cabecalho = ['COD', 'PRODUTO', 'DESCRIÇÃO', 'VALOR(R$)']
        escrever = csv.DictWriter(atlz, fieldnames=cabecalho)

        if atlz.tell() == 0:
            escrever.writeheader()

        for i in atz:
            escrever.writerow(
                {'COD': i['COD'], 'PRODUTO': i['PRODUTO'],
                 'DESCRIÇÃO': i['DESCRIÇÃO'], 'VALOR(R$)': i['VALOR(R$)']}
            )


def controle_caixa(nome, cp, ct):
    """
    Função que tem como objetivo criar um controle que permita armezanar os dados
    do caixa.
    :param nome: Nome do operador que estara utilizando o caixa
    :param cp: Contrlo dos valores em R$ parciais do caixa
    :param ct: Controle do valor total do caixa depois do fechamento

    """
    with open('bd_controle_caixa.csv', 'a', newline='', encoding='utf-8') as salvar:
        cabecalho = ['OPR', 'DATA', 'HORA', 'CAIXA_PARCIAL', 'CAIXA_TOTAL']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow({'OPR': nome[0], 'DATA': dh.datas(), 'HORA': dh.horas(),
                           'CAIXA_PARCIAL': cp, 'CAIXA_TOTAL': ct})


def abrir_controle_caixa():
    """
    Função que tem como objetivo abrir o arquivo csv em modo leitura
    :return: Retorna uma lista com os dados no modo dict do arquivo csv
    bd_controle_caixa.csv

    """
    with open('bd_controle_caixa.csv', 'r', newline='', encoding='utf-8') as abrir:
        lista = []
        ler = csv.DictReader(abrir)

        for i in ler:
            lista.append(i)

        return lista


