from models import Contato, ContatoDAO

class View:
    @staticmethod
    def contato_inserir(nome, telefone, email, nascimento):
        ContatoDAO.inserir(Contato(0, nome, telefone, email, nascimento))

    @staticmethod
    def contato_listar():
        return ContatoDAO.listar()

    @staticmethod
    def contato_atualizar(id, nome, telefone, email, nascimento):
        contatos = ContatoDAO.listar()
        for contato in contatos:
            if contato.id == id:
                contato.nome = nome
                contato.telefone = telefone
                contato.email = email
                contato.nascimento = nascimento
                ContatoDAO.__salvar()
                return True
        return False
    
