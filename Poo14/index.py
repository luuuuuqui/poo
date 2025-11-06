from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.agendarservicoUI import AgendarServicoUI
from views import View

import streamlit as st


class IndexUI:
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        match op:
            case "Entrar no Sistema":
                LoginUI.main()
            case "Abrir Conta":
                AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu", ["Meus Dados", "Meus Serviços", "Agendar Serviço"]
        )
        match op:
            case "Meus Dados":
                PerfilClienteUI.main()
            case "Meus Serviços":
                PerfilClienteUI.meus_servicos()
            case "Agendar Serviço":
                AgendarServicoUI.main()

    @staticmethod
    def menu_profissional():
        op = st.sidebar.selectbox(
            "Menu", ["Meus Dados", "Horários", "Confirmar", "Criar Horário"]
        )
        match op:
            case "Meus Dados":
                PerfilProfissionalUI.main()
            case "Horários":
                PerfilProfissionalUI.horarios()
            case "Confirmar":
                PerfilProfissionalUI.confirmar()
            case "Criar Horário":
                PerfilProfissionalUI.abrir_agenda()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Cadastros", ["Clientes", "Serviços", "Profissionais", "Horários"]
        )
        match op:
            case "Clientes":
                ManterClienteUI.main()
            case "Serviços":
                ManterServicoUI.main()
            case "Profissionais":
                ManterProfissionalUI.main()
            case "Horários":
                ManterHorarioUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_tipo"] == "admin"
            tipo_usuario = st.session_state.get("usuario_tipo", "cliente")

            st.sidebar.write(
                "Bem-vindo(a), " + st.session_state["usuario_nome"].split()[0] + "!"
            )
            if admin:
                IndexUI.menu_admin()
            elif tipo_usuario == "profissional":
                IndexUI.menu_profissional()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()


IndexUI.main()
