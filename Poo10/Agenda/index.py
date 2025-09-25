from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterprofissionalUI import ManterProfissionalUI
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_admin():            
        op = st.sidebar.selectbox("Cadastros", ["Clientes", "Serviços", "Profissional"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Profissional": ManterProfissionalUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()

IndexUI.main()