from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.manterhorarioUI import ManterHorarioUI
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_admin():            
        op = st.sidebar.selectbox("Cadastros", ["Clientes", "Serviços", "Profissional", "Horários"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Profissional": ManterProfissionalUI.main()
        if op == "Horários": ManterHorarioUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()

IndexUI.main()