def cliente_inserir(nome, email, fone, senha):
    cliente = Cliente(0, nome, email, fone, senha)
    ClienteDAO.inserir(cliente)

def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    ClienteDAO.atualizar(cliente)

def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    ClienteDAO.excluir(cliente)

def cliente_criar_admin():
    for c in View.cliente_listar():
        if c.get_email() == "admin": return
    View.cliente_inserir("admin", "admin", "fone", "1234")

def cliente_autenticar(email, senha):
    for c in View.cliente_listar():
        if c.get_email() == email and c.get_senha() == senha:
            return {"id": c.get_id(), "nome": c.get_nome()}
    return None
