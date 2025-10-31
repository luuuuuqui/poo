import streamlit as st
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            try: View.cliente_inserir(nome, email, fone, senha):
            except ValueError as e:
                st.error(f"Erro ao criar conta: {e}")
            else:
                st.success("Conta criada com sucesso")
                time.sleep(1)
                st.rerun()
