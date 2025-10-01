import streamlit as st
import pandas as pd
from views import View 
import time

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe o especialidade")
        conselho = st.text_input("Informe o conselho")
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, conselho)
            st.success("Profissional inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais, format_func=lambda x: str(x))
            if op is not None:
                nome = st.text_input("Informe o novo nome", op.get_nome())
                especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
                conselho = st.text_input("Informe o novo conselho", op.get_conselho())
                if st.button("Atualizar"):
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, especialidade, conselho)
                    st.success("Profissional atualizado com sucesso")
                    time.sleep(1)
                    st.rerun()

    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais, format_func=lambda x: str(x))
            if op is not None and st.button("Excluir"):
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(1)
                st.rerun()
