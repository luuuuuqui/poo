class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = fone

    def toString(self):
        return f'ID: {self.__id}, Nome: {self.__nome}, Email: {self.__email}, Telefone: {self.__telefone}'

