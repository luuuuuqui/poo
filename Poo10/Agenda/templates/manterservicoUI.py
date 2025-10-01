import streamlit as st
import pandas as pd
from views import View 
import time

class ManterServicoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Servicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    @staticmethod
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum Serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.number_input("Informe o valor (R$)", min_value=0.0, format="%.2f")
        if st.button("Inserir"):
            View.servico_inserir(descricao, valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum Serviço cadastrado")
        else:
            op = st.selectbox("Atualização de Serviços", servicos, format_func=lambda x: str(x))
            if op is not None:
                descricao = st.text_input("Informe a nova descrição", op.get_descricao())
                valor = st.number_input("Informe o novo valor (R$)", min_value=0.0, value=float(op.get_valor()), format="%.2f")
                if st.button("Atualizar"):
                    id = op.get_id()
                    View.servico_atualizar(id, descricao, valor)
                    st.success("Serviço atualizado com sucesso")
                    time.sleep(1)
                    st.rerun()

    @staticmethod
    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum Serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviços", servicos, format_func=lambda x: str(x))
            if op is not None and st.button("Excluir"):
                id = op.get_id()
                View.servico_excluir(id)
                st.success("Serviço excluído com sucesso")
                time.sleep(1)
                st.rerun()
