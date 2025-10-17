import json
import datetime

class Horario:
    def __init__(self, id: int, confirmado: bool, datahora: datetime.datetime, cliente: str, servico: str, profissional: str) -> None:
        self.set_id(id)
        self.set_confirmado(confirmado)
        self.set_datahora(datahora)
        self.set_idcliente(cliente)
        self.set_idservico(servico)
        self.set_idprofissional(profissional)
    
    def get_id(self) -> int: return self.__id
    def get_confirmado(self) -> bool: return self.__confirmado
    def get_datahora(self) -> datetime.datetime: return self.__datahora
    def get_idcliente(self) -> str: return self.__idcliente
    def get_idservico(self) -> str: return self.__idservico
    def get_idprofissional(self) -> str: return self.__idprofissional

    def set_id(self, id: int) -> None: self.__id = id
    def set_confirmado(self, confirmado: bool) -> None: self.__confirmado = confirmado
    def set_datahora(self, datahora: datetime.datetime) -> None: self.__datahora = datahora
    def set_idcliente(self, cliente: str) -> None: self.__idcliente = cliente
    def set_idservico(self, servico: str) -> None: self.__idservico = servico
    def set_idprofissional(self, profissional: str) -> None: self.__idprofissional = profissional

    @staticmethod
    def to_json(obj) -> dict:
        if not isinstance(obj, Horario):
            raise TypeError("Objeto não é do tipo Horario")
        dic = {
            "id": obj.get_id(),
            "confirmado": obj.get_confirmado(),
            "datahora": obj.get_datahora().isoformat() if obj.get_datahora() else None,
            "cliente": obj.get_idcliente(),
            "servico": obj.get_idservico(),
            "profissional": obj.get_idprofissional()
        }
        return dic
    
    @staticmethod
    def from_json(dic) -> object:
        datahora = None
        if dic["datahora"]:
            datahora = datetime.datetime.fromisoformat(dic["datahora"])
        return Horario(dic["id"], dic["confirmado"], datahora, dic["cliente"], dic["servico"], dic["profissional"])

    def __str__(self) -> str:
        return f"{self.__id} - {self.__confirmado} - {self.__datahora} - {self.__idcliente} - {self.__idservico} - {self.__idprofissional}"

class HorarioDAO():
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
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("horarios.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Horario.to_json)

