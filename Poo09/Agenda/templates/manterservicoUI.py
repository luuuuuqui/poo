import streamlit as st
import pandas as pd
from views import View 
import time

class ManterServicoUI:
    def main():
        st.header("Cadastro de Servicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar():
        Servicos = View.Servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Serviço cadastrado")
        else:
            list_dic = []
            for obj in Servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            View.Servico_inserir(descricao, valor)
            st.success("Servico inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        Servicos = View.Servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Servico cadastrado")
        else:
            op = st.selectbox("Atualização de Serviços", Servicos)
            descricao = st.text_input("Informe o nova descrição", op.get_descricao())
            valor = st.text_input("Informe o novo ", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Servico_atualizar(id, descricao, valor)
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        Servicos = View.Servico_listar()
        if len(Servicos) == 0: st.write("Nenhum Serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Servicos", Servicos)
            if st.button("Excluir"):
                id = op.get_id()
                View.Servico_excluir(id)
                st.success("Serviço excluído com sucesso")
                time.sleep(2)
                st.rerun()
