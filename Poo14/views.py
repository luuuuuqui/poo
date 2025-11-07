from datetime import datetime as dt

from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.profissional import Profissional, ProfissionalDAO
from models.horario import Horario, HorarioDAO


class View:
    # autenticação
    @staticmethod
    def autenticar(email, senha):
        if resultado := View.cliente_autenticar(email, senha):
            resultado["tipo"] = "cliente"
            return resultado

        elif resultado := View.profissional_autenticar(email, senha):
            resultado["tipo"] = "profissional"
            return resultado
        
    # Cliente
    @staticmethod
    def cliente_inserir(nome: str, email: str, fone: str, senha: str, nascimento: dt):
        if (
            any(
                c.get_email().lower().strip() == email.lower().strip()
                for c in View.cliente_listar() + View.profissional_listar()
            )
            or email.lower().strip() == "admin"
        ):
            raise ValueError("Email já cadastrado.")
        if fone is None:
            fone = ""
        try:
            ClienteDAO.inserir(Cliente(0, nome, email, fone, senha, nascimento))
        except ValueError as ve:
            raise ve

    @staticmethod
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key=lambda obj: obj.get_id())
        return r

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha, nascimento):
        cliente = Cliente(id, nome, email, fone, senha, nascimento)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        if any(h.get_idcliente() == id for h in HorarioDAO.listar()):
            raise ValueError(
                "Cliente possui horários agendados e não pode ser excluído."
            )
        cliente = Cliente(id, "", "", "", "", dt.now())
        ClienteDAO.excluir(cliente)

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome(), "email": c.get_email()}
        return None

    @staticmethod
    def cliente_listar_aniversariantes(mes):
        clientes = View.cliente_listar()
        r = []
        for p in clientes:
            nascimento = p.get_nascimento()
            if nascimento and (mes == 0 or nascimento.month == mes):
                r.append(
                    {
                        "id": p.get_id(),
                        "nome": p.get_nome(),
                        "nascimento": dt.strftime(nascimento, "%d/%m/%Y"),
                        "idade": f"{(dt.now() - nascimento).days // 365} anos",
                    }
                )
        return sorted(
            r,
            key=lambda d: (
                d["nascimento"].split("/")[1],
                d["nascimento"].split("/")[0],
            ),
        )

    @staticmethod
    def cliente_criar_admin():
        if not any(
            c.get_email().lower().strip() == "admin" for c in ClienteDAO.listar()
        ):
            View.cliente_inserir(
                "admin", "admin", "fone", "1234", dt.strptime("2000-01-01", "%Y-%m-%d")
            )

    @classmethod
    def cliente_admin_criar(cls):
        clientes = cls.cliente_listar()

        if not any(c.get_email() == "admin" for c in clientes):
            cls.cliente_inserir(
                "Administrador", "admin", "admin", "1234", dt(2000, 1, 1)
            )

    # Serviços
    @staticmethod
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    @staticmethod
    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key=lambda obj: obj.get_descricao())
        return r

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
    def profissional_inserir(nome, email, senha, especialidade, conselho, nascimento):
        if (
            any(
                c.get_email().lower().strip() == email.lower().strip()
                for c in View.cliente_listar() + View.profissional_listar()
            )
            or email.lower().strip() == "admin"
        ):
            raise ValueError("Email já cadastrado.")
        try:
            profissional = Profissional(
                0, nome, email, senha, especialidade, conselho, nascimento
            )
        except ValueError as ve:
            raise ve
        ProfissionalDAO.inserir(profissional)

    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key=lambda obj: obj.get_id())
        return r

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    @staticmethod
    def profissional_atualizar(
        id, nome, email, senha, especialidade, conselho, nascimento
    ):
        profissional = Profissional(
            id, nome, email, senha, especialidade, conselho, nascimento
        )
        ProfissionalDAO.atualizar(profissional)

    @staticmethod
    def profissional_excluir(id):
        if any(h.get_idprofissional() == id for h in HorarioDAO.listar()):
            raise ValueError(
                "Profissional possui horários agendados e não pode ser excluído."
            )
        profissional = Profissional(id, "", "", "", "", "", dt.now())
        ProfissionalDAO.excluir(profissional)

    @staticmethod
    def profissional_autenticar(email, senha):
        for usuario in View.profissional_listar():
            if usuario.get_email() == email and usuario.get_senha() == senha:
                return {"id": usuario.get_id(), "nome": usuario.get_nome()}
        return None

    @staticmethod
    def profissional_listar_aniversariantes(mes):
        profissionais = View.profissional_listar()
        r = []
        for p in profissionais:
            nascimento = p.get_nascimento()
            if nascimento and (mes == 0 or nascimento.month == mes):
                r.append(
                    {
                        "id": p.get_id(),
                        "nome": p.get_nome(),
                        "nascimento": dt.strftime(nascimento, "%d/%m/%Y"),
                        "idade": f"{(dt.now() - nascimento).days // 365} anos",
                    }
                )
        return sorted(
            r,
            key=lambda d: (
                d["nascimento"].split("/")[1],
                d["nascimento"].split("/")[0],
            ),
        )

    # Horários
    @staticmethod
    def horario_inserir(confirmado, datahora, idcliente, idservico, idprofissional):
        if any(
            h.get_idprofissional() == idprofissional and h.get_datahora() == datahora
            for h in HorarioDAO.listar()
        ):
            raise ValueError(
                "Esse profissional já possui um horário agendado para esta data e hora."
            )
        horario = Horario(0, confirmado, datahora, idcliente, idservico, idprofissional)
        HorarioDAO.inserir(horario)

    @staticmethod
    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key=lambda obj: obj.get_datahora())
        return r

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)

    @staticmethod
    def horario_listar_cliente(id_cliente):
        r = []
        for h in View.horario_listar():
            if h.get_idcliente() == id_cliente:
                r.append(h)
        return r

    @staticmethod
    def horario_listar_profissional(id_profissional):
        r = []
        for h in View.horario_listar():
            if h.get_idprofissional() == id_profissional:
                r.append(h)
        return r

    @staticmethod
    def horario_atualizar(
        id, confirmado, datahora, idcliente, idservico, idprofissional
    ):
        horario = Horario(
            id, confirmado, datahora, idcliente, idservico, idprofissional
        )
        HorarioDAO.atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        horario_existente = View.horario_listar_id(id)

        # Verifica se o horário existe
        if horario_existente is None:
            raise ValueError("Horário não encontrado.")

        # Verifica se o horário está agendado
        if horario_existente.get_idcliente() is not None:
            raise ValueError("Horário está agendado por um cliente.")

        horario = Horario(id, False, dt.now(), "", "", "")
        HorarioDAO.excluir(horario)

    @staticmethod
    def horario_agendar_horario(idprofissional):
        r = []
        agora = dt.now()
        for h in View.horario_listar():
            if (
                h.get_datahora() >= agora
                and h.get_confirmado() == False
                and h.get_idcliente() == None
                and h.get_idprofissional() == idprofissional
            ):
                r.append(h)
        r.sort(key=lambda h: h.get_datahora())
        return r
