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
    with open('bd_controle_caixa.csv', 'a', newline='', encoding='utf-8') as teste:
        cabecalho = ['OPR', 'DATA', 'HORA', 'CAIXA_PARCIAL', 'CAIXA_TOTAL']
        escrever = csv.DictWriter(teste, fieldnames=cabecalho)

        if teste.tell() == 0:
            escrever.writeheader()

        escrever.writerow({'OPR': nome[0], 'DATA': dh.datas(), 'HORA': dh.horas(),
                           'CAIXA_PARCIAL': cp[0], 'CAIXA_TOTAL': ct})
