import streamlit as st
import time
import datetime
import pandas as pd

from views import View

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())

        if st.button("Atualizar"):
            id = op.get_id()
            View.profissional_atualizar(id, nome, email, especialidade, conselho, senha)
            st.success("Seus dados foram atualizados com sucesso.")
    
    def horarios():
        st.header("Meus Horários")
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            clientes = {c.get_id(): c.get_nome() for c in View.cliente_listar()}
            servicos = {s.get_id(): s.get_descricao() for s in View.servico_listar()}
            for obj in horarios:
                if obj.get_idprofissional() != st.session_state["usuario_id"]:
                    continue
                dic = {
                    "id": obj.get_id(),
                    "confirmado": obj.get_confirmado(),
                    "datahora": obj.get_datahora().strftime("%d/%m/%Y %H:%M") if obj.get_datahora() else "",
                    "cliente": clientes.get(obj.get_idcliente(), obj.get_idcliente()),
                    "servico": servicos.get(obj.get_idservico(), obj.get_idservico()),
                }
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    def abrir_agenda():
        st.header("Criar Horário")

        op = View.profissional_listar_id(st.session_state["usuario_id"])

        datahora = None
        dia = st.date_input("Dia do atendimento (dd/mm/yy):", value=None, format="DD/MM/YYYY")
        inicio = st.time_input("Horário inicial (hh:mm):", value=None)
        fim = st.time_input("Horário final (mm):", value=None)
        intervalo = st.time_input("Intervalo entre atendimentos (hh:mm):", value=None)        
        
        
        if st.button("Inserir"):
            inicio_dt = datetime.datetime.combine(datetime.date.today(), inicio)
            
            delta_intervalo = datetime.timedelta(hours=intervalo.hour, minutes=intervalo.minute)
            
            while inicio_dt.time() <= (datetime.datetime.combine(dia, fim) - delta_intervalo).time():
                View.horario_inserir(False, datetime.datetime.combine(dia, inicio_dt.time()), None, None, op.get_id())
                inicio_dt += delta_intervalo
            st.text("x = " + str(inicio_dt.time()))
            st.text("inicio = " + str(inicio))

            st.success("Horário inserido com sucesso")
            #time.sleep(1)
            #st.rerun()