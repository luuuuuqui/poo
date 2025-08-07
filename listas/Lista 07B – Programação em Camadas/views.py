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
        return ContatoDAO.contato_atualizar(id, nome, telefone, email, nascimento)

    @staticmethod
    def contato_deletar(id):
        return ContatoDAO.contato_deletar(id)


if __name__ == "__main__":
    print("Você está executando a View diretamente. Use o módulo UI para interagir com a aplicação.")