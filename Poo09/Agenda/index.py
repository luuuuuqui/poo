from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
import streamlit as st

class IndexUI:

    @staticmethod
    def menu_admin():            
        op = st.sidebar.selectbox("Cadastros", ["Clientes", "Serviços"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()

    @staticmethod
    def sidebar():
        IndexUI.menu_admin()

    @staticmethod
    def main():
        IndexUI.sidebar()

IndexUI.main()