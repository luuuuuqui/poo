from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.profissional import Profissional, ProfissionalDAO
from models.horario import Horario, HorarioDAO


class View:
    # autenticação
    @staticmethod
    def autenticar(email, senha):
        resultado = View.cliente_autenticar(email, senha)
        if resultado:
            resultado["tipo"] = "cliente"
            resultado["id"] = resultado["id"]
            return resultado
        
        resultado = View.profissional_autenticar(email, senha)
        if resultado:
            resultado["tipo"] = "profissional"
            resultado["id"] = resultado["id"]
            return resultado

    # Cliente 
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    @staticmethod
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")

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
    def profissional_inserir(nome, email, senha, especialidade, conselho):
        profissional = Profissional(0, nome, email, senha, especialidade, conselho)
        ProfissionalDAO.inserir(profissional)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, senha, especialidade, conselho):
        profissional = Profissional(id, nome, email, senha, especialidade, conselho)
        ProfissionalDAO.atualizar(profissional)

    @staticmethod
    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(profissional)

    @staticmethod
    def profissional_autenticar(email, senha):
        for usuario in View.profissional_listar():
            if usuario.get_email() == email and usuario.get_senha() == senha:
                return {"id": usuario.get_id(), "nome": usuario.get_nome()}
        return None
    
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

    
