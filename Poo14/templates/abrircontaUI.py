import streamlit as st
from views import View
import time
from datetime import datetime as dt


class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")

        nascimento = dt.combine(
            st.date_input(label="Informe a data de nascimento", format="DD/MM/YYYY"), dt.min.time()
        )
        if not nome:
            st.error("O nome deve ser preenchido.")
        elif not email:
            st.error("O e-mail deve ser preenchido.")
        elif not senha:
            st.error("A senha deve ser preenchida.")
        elif nascimento >= dt.now():
            st.error("A data de nascimento deve ser no passado.")
        elif st.button("Inserir"):
            try:
                View.cliente_inserir(nome, email, fone, senha, nascimento)
            except ValueError as e:
                st.error(f"Erro ao criar conta: {e}")
            else:
                st.success("Conta criada com sucesso")
                time.sleep(1)
                st.rerun()
