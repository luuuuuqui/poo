import json
from typing import List, Optional

class Cliente:
    def __init__(self, id, nome, fone, email):
        self.__id = id
        self.__nome = nome
        self.__fone = fone
        self.__email = email

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_fone(self):
        
        return self.__fone
    
    def get_email(self):
        return self.__email
    
    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("O ID deve ser um número inteiro")
    
    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome
        else:
            raise ValueError("O nome deve ser uma string")

    def set_fone(self, fone):
        if isinstance(fone, str):
            self.__fone = fone
        else:
            raise ValueError("O telefone deve ser válido.")

    def set_email(self, email):
        if isinstance(email, str):
            self.__email = email
        else:
            raise ValueError("O email deve ser válido.")
        
    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self.__nome,
            'fone': self.__fone,
            'email': self.__email
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['id'], data['nome'], data['fone'], data['email'])

