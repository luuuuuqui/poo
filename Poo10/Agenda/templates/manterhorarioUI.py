import streamlit as st
import pandas as pd
from views import View 
import time
import datetime

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de Horarios")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    @staticmethod
    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        confirmado = st.checkbox("Confirmado")
        d = st.date_input("Dia do atendimento:", value=None)
        t = st.time_input("Horário do atendimento:", value=None)

        if d is not None and t is not None:
            datahora = datetime.datetime(d.year, d.month, d.day, t.hour, t.minute, t.second)
            st.success(f"Data e hora selecionada: {datahora}")
        else:
            st.warning("Selecione o dia e o horário do atendimento.")

        clientes = View.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else: cliente = st.selectbox("Selecione o cliente", clientes, format_func=lambda x: str(x))
        
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else: servico = st.selectbox("Selecione o serviço", servicos, format_func=lambda x: str(x))
        
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else: profissional = st.selectbox("Selecione o profissional", profissionais, format_func=lambda x: str(x))

        if not datahora and cliente and not servico and not profissional:
            st.warning("Preencha todos os campos")
        
        if st.button("Inserir"):
            View.horario_inserir(confirmado, datahora, cliente.get_id(), servico.get_id(), profissional.get_id())
            st.success("Horário inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horario cadastrado")
        else:
            op = st.selectbox("Atualização de Horários", horarios, format_func=lambda x: str(x))
            if op is not None:
                nome = st.text_input("Informe o novo nome", op.get_nome())
                email = st.text_input("Informe o novo e-mail", op.get_email())
                fone = st.text_input("Informe o novo fone", op.get_fone())
                if st.button("Atualizar"):
                    id = op.get_id()
                    View.horario_atualizar(id, nome, email, fone)
                    st.success("Horario atualizado com sucesso")
                    time.sleep(1)
                    st.rerun()

    @staticmethod
    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horario cadastrado")
        else:
            op = st.selectbox("Exclusão de Horarios", horarios, format_func=lambda x: str(x))
            if op is not None and st.button("Excluir"):
                id = op.get_id()
                View.horario_excluir(id)
                st.success("Horario excluído com sucesso")
                time.sleep(1)
                st.rerun()
