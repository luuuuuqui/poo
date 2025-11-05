import streamlit as st
import pandas as pd
from sympy import N
from views import View
import time
from datetime import datetime as dt

class PerfilClienteUI:
    @staticmethod
    def main():
        st.header("Meus Dados")
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        if op:
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            fone = st.text_input("Informe o novo fone", op.get_fone())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            nascimento = dt.combine(
                st.date_input(
                    label="Informe a nova data de nascimento",
                    value=op.get_nascimento().date() if op.get_nascimento() else dt.today().date()
                ),
                dt.min.time()
            )

        if st.button("Atualizar"):
            try:
                if op:
                    View.cliente_atualizar(op.get_id(), nome, email, fone, senha, nascimento)
                    st.success("Dados atualizados com sucesso")
            except ValueError as e:
                st.error(f"Erro ao atualizar dados: {e}")
            else:
                time.sleep(1)
                st.rerun()
    
    @staticmethod
    def meus_servicos():
        st.header("Meus Serviços")
        horarios = View.horario_listar_cliente(st.session_state["usuario_id"])
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            servicos = {s.get_id(): s.get_descricao() for s in View.servico_listar()}
            profissionais = {p.get_id(): p.get_nome() for p in View.profissional_listar()}
            for obj in horarios:
                dic = {
                    "id": obj.get_id(),
                    "confirmado": obj.get_confirmado(),
                    "datahora": obj.get_datahora().strftime("%d/%m/%Y %H:%M") if obj.get_datahora() else "",
                    "servico": servicos.get(obj.get_idservico(), obj.get_idservico()),
                    "profissional": profissionais.get(obj.get_idprofissional(), obj.get_idprofissional())
                }
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)