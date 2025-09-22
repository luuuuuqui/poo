import json

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):

        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    
    def get_id(self) -> int: return self.__id
    def get_nome(self) -> str: return self.__nome
    def get_email(self) -> str: return self.__email
    def get_fone(self) -> str: return self.__fone

    def set_id(self, id) -> None: self.__id = id
    def set_nome(self, nome) -> None: self.__nome = nome
    def set_email(self, email) -> None: self.__email = email
    def set_fone(self, fone) -> None: self.__fone = fone

    def to_json(self) -> dict:
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone}
        return dic
    
    @staticmethod
    def from_json(dic) -> object:
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ClienteDAO():
    __objetos = []

    @classmethod
    def inserir(cls, obj) -> None:
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id) -> object:
        cls.abrir()
        for obj in cls.__objetos: 
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls) -> None:
        cls.__objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Cliente.to_json)  

