import json
import os
from datetime import datetime

'''
id : {nome, email, fone, nascimento}
'''

class Contato:
    def __init__(self):
        self.__contatos = {}
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__fone = ""
        self.__nascimento = datetime.now()
    
    def adcionar(self, contato):
        id = len(self.__contatos) + 1
        while self.__contatos.get(id) is not None:
            id += 1
        self.__contatos[id] = contato
        print(f"{self.__contatos}")
        return id

    def remover(self, id: int):
        if id in self.__contatos:
            del self.__contatos[id]
    

    def atualizar(self, id: int, contato):
        if id in self.__contatos:
            self.__contatos[id] = contato
            return True
        return False
    # métodos


    # toString, to_dict w from_dict
    def toString(self):
        print(f"{self.__contatos}")
        string = ""
        for id, contato in self.__contatos:
            string += f"ID: {id}, Nome: {contato[0]}, Email: {contato[1]}, Telefone: {contato[2]}, Nascimento: {contato[3].strftime('%d/%m/%Y')}\n"
        if not self.__contatos:
            return "Nenhum contato cadastrado."
        return string
    
    def to_dict(self) -> dict:
        return {
            'id': self.__id,
            'nome': self.__nome,
            'email': self.__email,
            'fone': self.__fone
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['id'], data['nome'], data['email'], data['fone'])
    

class ContatoUI:
    @staticmethod
    def adicionar_contato():
        try:
            nome = input("Digite o nome do contato: ").strip()
            if not nome:
                raise ValueError("Nome não pode ser vazio.")
            
            email = input("Digite o email do contato: ").strip()
            if not email:
                raise ValueError("Email não pode ser vazio.")
            
            fone = input("Digite o telefone do contato: ").strip()
            if not fone:
                raise ValueError("Telefone não pode ser vazio.")
            
            nascimento = datetime.strptime(input("Digite a data de nascimento (dd/mm/yyyy): ").strip(), "%d/%m/%Y")
            if nascimento > datetime.now():
                raise ValueError("Data de nascimento não pode ser no futuro.")
            
        
            novo_contato = [nome, email, fone, nascimento]
            print(f"Novo contato: {novo_contato}")
            c = Contato()

            id = c.adcionar(novo_contato)
            print(f"Contato adicionado com sucesso! ID: {id}")
        
        except ValueError as e:
            print(f"Erro ao adicionar contato: {e}")
    
    @staticmethod
    def remover_contato():
        self.__contato.remover(id)

    @staticmethod
    def atualizar_contato():
        contato = Contato(id=id, nome=nome, email=email, fone=fone)
        return self.__contato.atualizar(id, contato)
    
    @staticmethod
    def listar_contatos():
        c = Contato()
        print(f'{c.toString()}')

if __name__ == "__main__":
    ContatoUI.adicionar_contato()
    ContatoUI.listar_contatos()

