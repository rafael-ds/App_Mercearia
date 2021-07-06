class Usuario:
    numero_id = 0

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
