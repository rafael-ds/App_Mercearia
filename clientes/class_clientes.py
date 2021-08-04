import csv


class Clientes:
    def __init__(self, nome, telefone, email, cpf):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf

    def nome(self):
        return self.__nome

    def telefone(self):
        return self.__telefone

    def email(self):
        return self.__email

    def cpf(self):
        return self.__cpf


def cad_cliente(cliente):
    with open('bd_cliente.csv', 'a', encoding='utf-8', newline='') as salvar:
        cabecalho = ['NOME', 'TEL.', 'EMAIL', 'CPF']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(cliente)


def lista_clientes():
    lista = []

    with open('bd_cliente.csv', 'r', encoding='utf-8', newline='') as abrir:
        ler = csv.DictReader(abrir)

        for i in ler:
            lista.append(i)

    return lista

