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
            date=st.date_input(
                label="Informe a data de nascimento",
                format="DD/MM/YYYY",
                value=dt(2000, 1, 1),
                min_value=dt(1900, 1, 1),
                max_value=dt.today(),
            ),
            time=dt.min.time(),
        )
        
        if st.button("Inserir"):
            if nome and email and senha and nascimento:
                if not fone: fone = "0"
                try:
                    View.cliente_inserir(nome, email, fone, senha, nascimento)
                    st.success("Conta criada com sucesso")
                    time.sleep(1)
                    st.rerun()
                except ValueError as e:
                    st.error(f"Erro ao criar conta: {e}")
            else:
                if not nome:
                    st.error("O nome deve ser preenchido.")
                if not email:
                    st.error(body="O e-mail deve ser preenchido.")
                if not senha:
                    st.error("A senha deve ser preenchida.")
                if not nascimento:
                    st.error("A data de nascimento deve ser preenchida.")
                elif nascimento >= dt.now():
                    st.error("A data de nascimento deve ser no passado.")