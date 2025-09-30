from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.profissional import Profissional, ProfissionalDAO
from models.horario import Horario, HorarioDAO


class View:
    # Cliente 
    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    # Serviços
    @staticmethod
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    @staticmethod
    def servico_listar():
        return ServicoDAO.listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico = Servico(id, "", 0)
        ServicoDAO.excluir(servico)

    # Profissionais
    @staticmethod
    def profissional_inserir(nome, especialidade, conselho):
        profissional = Profissional(0, nome, especialidade, conselho)
        ProfissionalDAO.inserir(profissional)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, especialidade, conselho):
        profissional = Profissional(id, nome, especialidade, conselho)
        ProfissionalDAO.atualizar(profissional)

    @staticmethod
    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(profissional)
    
    # Horários
    @staticmethod
    def horario_inserir(confirmado, datahora, idcliente, idservico, idprofissional):
        horario = Horario(0, confirmado, datahora, idcliente, idservico, idprofissional)
        HorarioDAO.inserir(horario)
    
    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()
    
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
    
    @staticmethod
    def horario_atualizar(id, confirmado, datahora, idcliente, idservico, idprofissional):
        horario = Horario(id, confirmado, datahora, idcliente, idservico, idprofissional)
        HorarioDAO.atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        horario = Horario(id, False, None, "", "", "")
        HorarioDAO.excluir(horario)
