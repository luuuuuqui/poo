import json
from datetime import datetime

class Contato:
    def __init__(self, id, nome, telefone, email, nascimento):
        self.id: int = id
        self.nome: str = nome
        self.telefone: str = telefone
        self.email: str = email
        self.nascimento: datetime = datetime.strptime(nascimento, "%d/%m/%Y")

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome} - Telefone: {self.telefone} - Email: {self.email} - Nascimento: {self.nascimento.strftime("%d/%m/%Y")}'

class ContatoDAO:
    __objetos = []
    
    @classmethod
    def inserir(cls, obj: Contato):
        cls.__abrir() 
        id = 0
        for aux in cls.__objetos:
            if aux.id > id:
                id = aux.id
        obj.id = id + 1   
        cls.__objetos.append(obj)
        cls.__salvar()

    @classmethod
    def listar(cls):
        cls.__abrir()
        return cls.__objetos

    @classmethod
    def deletar(cls, id):
        cls.__abrir()
        antes = len(cls.__objetos)
        cls.__objetos = [contato for contato in cls.__objetos if contato.id != id]
        if len(cls.__objetos) < antes:
            cls.__salvar()
            return True
        return False

    @classmethod
    def atualizar(cls, id, nome, telefone, email, nascimento):
        cls.__abrir()
        for contato in cls.__objetos:
            if contato.id == id:
                if nome is not None:
                    contato.nome = nome
                if telefone is not None:
                    contato.telefone = telefone
                if email is not None:
                    contato.email = email
                if nascimento is not None:
                    contato.nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
                cls.__salvar()
                return True
        return False

    @classmethod
    def __abrir(cls):
        cls.__objetos = []
        try:
            with open('contatos.json', 'r', encoding='utf-8') as file:
                conteudo = file.read().strip()
                if not conteudo:
                    return
                lista = json.loads(conteudo)
                for dic in lista:
                    obj = Contato(dic['id'], dic['nome'], dic['telefone'], dic['email'], dic['nascimento'])
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass
    
    @classmethod
    def __salvar(cls):
        with open('contatos.json', 'w', encoding='utf-8') as arquivo:
            lista = []
            for obj in cls.__objetos:
                dic = {
                    'id': obj.id,
                    'nome': obj.nome,
                    'telefone': obj.telefone,
                    'email': obj.email,
                    'nascimento': obj.nascimento.strftime("%d/%m/%Y")
                }
                lista.append(dic)
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("Você está executando o Models diretamente. Use o módulo UI para interagir com a aplicação.")