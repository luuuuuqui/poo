import json
from datetime import datetime as dt
from .dao import DAO


class Profissional:
    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        senha: str,
        especialidade: str,
        conselho: str,
        nascimento: dt,
    ):
        if nome is None or not str(nome).strip():
            raise ValueError("Nome deve ser preenchido.")
        if email is None or not str(email).strip():
            raise ValueError("E-mail deve ser preenchido.")
        if senha is None or not str(senha).strip():
            raise ValueError("Senha deve ser preenchida.")
        # nascimento opcional (permite usar objetos placeholder em excluir/atualizar)
        if nascimento is None:
            raise ValueError("Nascimento deve ser preenchido.")
        if not isinstance(nascimento, dt):
            raise ValueError("Nascimento deve ser uma data.")
        if nascimento >= dt.now():
            raise ValueError("Nascimento deve ser uma data no passado.")
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_nascimento(nascimento)

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_senha(self) -> str:
        return self.__senha

    def get_especialidade(self) -> str:
        return self.__especialidade

    def get_conselho(self) -> str:
        return self.__conselho

    def get_nascimento(self) -> dt:
        return self.__nascimento

    def set_id(self, id) -> None:
        self.__id = id

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def set_email(self, email) -> None:
        self.__email = email

    def set_senha(self, senha) -> None:
        self.__senha = senha

    def set_especialidade(self, especialidade) -> None:
        self.__especialidade = especialidade

    def set_conselho(self, conselho) -> None:
        self.__conselho = conselho

    def set_nascimento(self, nascimento) -> None:
        self.__nascimento = nascimento

    def to_json(self) -> dict:
        dic = {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "nascimento": self.__nascimento.isoformat() if isinstance(self.__nascimento, dt) else self.__nascimento
        }
        return dic

    @staticmethod
    def from_json(dic) -> object:
        if isinstance(dic["nascimento"], str):
            nasc = dt.fromisoformat(dic["nascimento"])
        else:
            nasc = dic["nascimento"]
        return Profissional(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["senha"],
            dic["especialidade"],
            dic["conselho"],
            nasc,
        )

    def __str__(self) -> str:
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha} - {self.__especialidade} - {self.__conselho} - {self.__nascimento}"


class ProfissionalDAO(DAO):
    @classmethod
    def abrir(cls) -> None:
        cls._objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Profissional.to_json)
