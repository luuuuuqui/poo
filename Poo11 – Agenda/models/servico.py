import json

class Servico:
    def __init__(self, id: int, descricao: str, valor: float):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def get_id(self) -> int: return self.__id
    def get_descricao(self) -> str: return self.__descricao
    def get_valor(self) -> float: return self.__valor

    def set_id(self, id: int) -> None: self.__id = id
    def set_descricao(self, descricao: str) -> None: self.__descricao = descricao
    def set_valor(self, valor: float) -> None: self.__valor = valor

    def to_json(self) -> dict:
        dic = {"id":self.__id, "descricao":self.__descricao, "valor":self.__valor}
        return dic

    @staticmethod
    def from_json(dic) -> object:
        return Servico(dic["id"], dic["descricao"], dic["valor"])

    def __str__(self) -> str:
        return f"{self.__id} - {self.__descricao} - {self.__valor}"

class ServicoDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj: Servico) -> None:
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
    def listar_id(cls, id: int) -> object:
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj: Servico) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj: Servico) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls) -> None:
        cls.__objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Servico.to_json)

