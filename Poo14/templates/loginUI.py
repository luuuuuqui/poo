import streamlit as st
from views import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            if email and senha:
                usuario = View.autenticar(email, senha)
                if usuario == None: st.error("E-mail ou senha inválidos")
                else:
                    st.session_state["usuario_id"] = usuario["id"]
                    st.session_state["usuario_nome"] = usuario["nome"]
                    if usuario["id"] != 0: st.session_state["usuario_tipo"] = usuario["tipo"]
                    else: st.session_state["usuario_tipo"] = "admin"
                    st.rerun()
            else:
                st.error("Preencha o e-mail e senha.")