import streamlit as st
import pandas as pd
from views import View 
import time
from datetime import datetime as dt

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Aniversários"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
        with tab5: ManterClienteUI.aniversarios()

    @staticmethod
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        nascimento = dt.combine(st.date_input(label="Informe a data de nascimento", format="DD/MM/YYYY", value=dt(2000, 1, 1), min_value=dt(1900, 1, 1), max_value=dt.today()), dt.min.time())
        if st.button("Inserir"):
            try:
                View.cliente_inserir(nome, email, fone, senha, nascimento)
            except Exception as e:
                st.error("Erro ao inserir cliente: {}".format(e))
            else:
                st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            if op:
                if st.session_state["usuario_id"] != op.get_id():
                    nome = st.text_input("Novo nome", op.get_nome())
                    email = st.text_input("Novo e-mail", op.get_email())
                    fone = st.text_input("Novo fone", op.get_fone())
                    nascimento = dt.combine(st.date_input(label="Nova data de nascimento", format="DD/MM/YYYY", value=op.get_nascimento(), min_value=dt(1900, 1, 1), max_value=dt.today()), dt.min.time())
                senha = st.text_input("Nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            if op:
                id = op.get_id()
                if View.cliente_atualizar(id, nome, email, fone, senha, nascimento):
                    st.success("Cliente atualizado com sucesso")
                else: st.error("Erro ao atualizar cliente. Tente novamente.")

    @staticmethod
    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox(
                "Exclusão de Profissionais", 
                clientes, 
                format_func=lambda p: f"{p.get_id()} - {p.get_nome()}"
        )
            if op is not None and st.button("Excluir"):
                id = op.get_id()
                if View.cliente_excluir(id):
                    st.success("Cliente excluído com sucesso")
                else: st.error("Erro ao excluir cliente. Tente novamente.")
                time.sleep(1)
                st.rerun()

    @staticmethod
    def aniversarios():
        if any(dt.now().strftime("%d/%m") == a['nascimento'][0:5] for a in View.cliente_listar_aniversariantes(0)):
            st.header(f"Aniversariantes do dia: {dt.today().strftime('%d/%m/%Y')}")
            
            for a in View.cliente_listar_aniversariantes(dt.now().month):
                if dt.now().strftime("%d/%m") == a['nascimento'][0:5]:
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"- {a['nome']} - {a['idade']}")
                    
                    with col2:
                        email = str(View.cliente_listar_id(a["id"])).split(" - ")[2]
                        nome = a['nome']
                        
                        st.link_button("Enviar email", f"mailto:{email}?subject=Feliz Aniversário!&body=Feliz Aniversário, {nome.split()[0]}!", use_container_width=True)
                    
                    
        
        st.header("Profissionais Aniversariantes do Mês")
        meses = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes = st.selectbox("Selecione o mês", range(len(meses)), format_func=lambda x: meses[x])
        aniversarios = View.cliente_listar_aniversariantes(mes)

        if len(aniversarios) == 0:
            st.write("Nenhum cliente faz aniversário neste mês.")
        else:
            df = pd.DataFrame(aniversarios)
            st.dataframe(df, hide_index=True)
