import csv


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
    with open('cad_prod.csv', 'a', encoding='utf-8', newline='') as salvar:
        cabecalho = ['COD', 'PRODUTO', 'DESCRIÇÃO', 'VALOR(R$)']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(produto)
