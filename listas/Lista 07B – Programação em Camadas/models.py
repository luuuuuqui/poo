import json
import datetime

class Contato:
    def __init__(self, id, nome, telefone, email, nascimento):
        self.id: int = id
        self.nome: str = nome
        self.telefone: str = telefone
        self.email: str = email
        self.nascimento: datetime = nascimento

    def __str__(self):
        return f'Nome: {self.nome} - Telefone: {self.telefone}'
    

class ContatoDAO:
    __objetos = []
    @classmethod
    def inserir(cls, obj: Contato):
        cls.__abrir() 
        id = 0
        for aux in cls.__objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1   
        cls.__objetos.append(obj)
        cls.__salvar()

    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__objetos

    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try:
            with open('contatos.json', 'r') as file:
                lista = json.load(file)
                for dic in lista:
                    obj = Contato(dic['id'], dic['nome'], dic['telefone'])
                    obj.id = dic['id']
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def __salvar(cls):
        with open('contatos.json', 'w') as arquivo:
            json.dump(cls.__ojetos, arquivo, default = vars)