import json

class Profissional:
    def __init__(self, id: int, nome: str, especialidade: str, conselho: str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
    
    def get_id(self) -> int: return self.__id
    def get_nome(self) -> str: return self.__nome
    def get_especialidade(self) -> str: return self.__especialidade
    def get_conselho(self) -> str: return self.__conselho

    def set_id(self, id) -> None: self.__id = id
    def set_nome(self, nome) -> None: self.__nome = nome
    def set_especialidade(self, especialidade) -> None: self.__especialidade = especialidade
    def set_conselho(self, conselho) -> None: self.__conselho = conselho

    def to_json(self) -> dict:
        dic = {"id":self.__id, "nome":self.__nome, "especialidade":self.__especialidade, "conselho":self.__conselho}
        return dic
    
    @staticmethod
    def from_json(dic) -> object:
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"])

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho}"

class ProfissionalDAO():
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
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Profissional.to_json)  

