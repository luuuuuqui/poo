import streamlit as st
import pandas as pd
from views import View 
import time
from datetime import datetime as dt

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Aniversariantes"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()
        with tab5: ManterProfissionalUI.aniversarios()

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
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        especialidade = st.text_input("Informe o especialidade")
        conselho = st.text_input("Informe o conselho")
        nascimento = dt.combine(st.date_input(label="Informe a data de nascimento"), dt.min.time())
        if st.button("Inserir"):
            try: View.profissional_inserir(nome, email, senha, especialidade, conselho, nascimento)
            except ValueError as e:
                st.error(f"Erro ao inserir profissional: {e}")
            else:
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
                email = st.text_input("Informe o novo e-mail", op.get_email())
                senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
                especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
                conselho = st.text_input("Informe o novo conselho", op.get_conselho())
                nascimento = dt.combine(st.date_input(label="Informe a data de nascimento"), dt.min.time())
                if st.button("Atualizar"):
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, email, senha, especialidade, conselho, nascimento)
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
                try: View.profissional_excluir(id)
                except ValueError as e:
                    st.error(f"Erro ao excluir profissional: {e}")
                else:
                    st.success("Profissional excluído com sucesso")
                time.sleep(1)
                st.rerun()

    @staticmethod
    def aniversarios():
        if any(dt.now().strftime("%d/%m") == a['nascimento'][0:5] for a in View.profissional_listar_aniversariantes(0)):
            st.write(f"Aniversariantes do dia: {dt.today().strftime('%d/%m')}")
            for a in View.profissional_listar_aniversariantes(dt.now().month):
                if dt.now().strftime("%d/%m") == a['nascimento'][0:5]:
                    st.markdown(f"- {a['nome']}")

        st.header("Profissionais Aniversariantes do Mês")
        meses = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes = st.selectbox("Selecione o mês", range(len(meses)), format_func=lambda x: meses[x])
        aniversarios = View.profissional_listar_aniversariantes(mes)

        if len(aniversarios) == 0:
            st.write("Nenhum profissional faz aniversário neste mês.")
        else:
            df = pd.DataFrame(aniversarios)
            st.dataframe(df, hide_index=True)
