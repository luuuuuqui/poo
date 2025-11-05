import streamlit as st
from views import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            usuario = View.autenticar(email, senha)
            if usuario == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = usuario["id"]
                st.session_state["usuario_nome"] = usuario["nome"]
                st.session_state["usuario_tipo"] = usuario["tipo"]
                st.rerun()