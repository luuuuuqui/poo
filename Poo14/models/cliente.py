import json
from datetime import datetime as dt
from .dao import DAO


class Cliente:
    def __init__(
        self, id: int, nome: str, email: str, fone: str, senha: str, nascimento: dt
    ):
        # validações individuais para campos obrigatórios
        if nome is None or not str(nome).strip():
            raise ValueError("Nome deve ser preenchido.")
        if email is None or not str(email).strip():
            raise ValueError("E-mail deve ser preenchido.")
        if senha is None or not str(senha).strip():
            raise ValueError("Senha deve ser preenchida.")
        if nascimento is None:
            raise ValueError("Nascimento deve ser preenchido.")
        if not isinstance(nascimento, dt):
            raise ValueError("Nascimento deve ser uma data.")
        if nascimento >= dt.now():
            raise ValueError("Nascimento deve ser uma data no passado.")
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_nascimento(nascimento)

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_fone(self) -> str:
        return self.__fone

    def get_senha(self) -> str:
        return self.__senha

    def get_nascimento(self) -> dt:
        return self.__nascimento

    def set_id(self, id) -> None:
        self.__id = id

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def set_email(self, email) -> None:
        self.__email = email

    def set_fone(self, fone) -> None:
        self.__fone = fone

    def set_senha(self, senha) -> None:
        self.__senha = senha

    def set_nascimento(self, nascimento) -> None:
        self.__nascimento = nascimento

    def to_json(self) -> dict:
        dic = {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha,
            "nascimento": self.__nascimento,
        }
        return dic

    @staticmethod
    def from_json(dic) -> object:
        if isinstance(dic["nascimento"], str):
            nasc = dt.fromisoformat(dic["nascimento"])
        return Cliente(
            dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"], nasc
        )

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha} - {self.__nascimento}"


class ClienteDAO(DAO):
    @classmethod
    def abrir(cls) -> None:
        DAO._objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    DAO._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Cliente.to_json)
