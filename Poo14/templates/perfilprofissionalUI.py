import streamlit as st
import time
import datetime
import pandas as pd

from views import View


class PerfilProfissionalUI:
    @staticmethod
    def main():
        st.header("Meus Dados")
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        if op:
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            senha = st.text_input(
                "Informe a nova senha", op.get_senha(), type="password"
            )
            especialidade = st.text_input(
                "Informe a nova especialidade", op.get_especialidade()
            )
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            nascimento = datetime.datetime.combine(
                st.date_input(
                    label="Informe a nova data de nascimento",
                    value=(
                        op.get_nascimento().date()
                        if op.get_nascimento()
                        else datetime.datetime.today().date()
                    ),
                ),
                datetime.datetime.min.time(),
            )

        if st.button("Atualizar"):
            if op:
                id = op.get_id()
            try:
                View.profissional_atualizar(
                    id, nome, email, especialidade, conselho, senha, nascimento
                )
            except ValueError as e:
                st.error(f"Erro ao atualizar seus dados: {e}")
            else:
                st.success("Seus dados foram atualizados com sucesso.")

    @staticmethod
    def horarios():
        st.header("Meus Horários")
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            clientes = {c.get_id(): c.get_nome() for c in View.cliente_listar()}
            servicos = {s.get_id(): s.get_descricao() for s in View.servico_listar()}

            horarios = View.horario_listar_profissional(st.session_state["usuario_id"])
            if len(horarios) == 0:
                st.write("Nenhum horário cadastrado")
            else:
                list_dic = []
                clientes = {c.get_id(): c.get_nome() for c in View.cliente_listar()}
                servicos = {
                    s.get_id(): s.get_descricao() for s in View.servico_listar()
                }
                for obj in horarios:
                    dic = {
                        "id": obj.get_id(),
                        "confirmado": obj.get_confirmado(),
                        "datahora": (
                            obj.get_datahora().strftime("%d/%m/%Y %H:%M")
                            if obj.get_datahora()
                            else ""
                        ),
                        "cliente": clientes.get(
                            obj.get_idcliente(), obj.get_idcliente()
                        ),
                        "servico": servicos.get(
                            obj.get_idservico(), obj.get_idservico()
                        ),
                    }
                    list_dic.append(dic)
                df = pd.DataFrame(list_dic)
                st.dataframe(df, hide_index=True)

    @staticmethod
    def abrir_agenda():
        st.header("Criar Horário")

        op = View.profissional_listar_id(st.session_state["usuario_id"])

        datahora = None
        dia = st.date_input(
            "Dia do atendimento (dd/mm/yy):", value=None, format="DD/MM/YYYY"
        )
        inicio = st.time_input("Horário inicial (hh:mm):", value=None)
        fim = st.time_input("Horário final (mm):", value=None)
        delta_intervalo = st.time_input("Intervalo entre atendimentos (hh:mm):", value=None)

        if st.button("Inserir"):
            try:
                inicio_atendimentos = datetime.datetime.combine(datetime.date.today(), inicio)
                delta_intervalo = datetime.timedelta(
                    hours=delta_intervalo.hour, minutes=delta_intervalo.minute
                )

                while (
                    inicio_atendimentos.time()
                    <= (datetime.datetime.combine(dia, fim) - delta_intervalo).time()
                ):
                    View.horario_inserir(
                        False,
                        datetime.datetime.combine(dia, inicio_atendimentos.time()),
                        None,
                        None,
                        op.get_id(),
                    )
                    inicio_atendimentos += delta_intervalo
                st.success("Horário inserido com sucesso")
            except ValueError as e:
                st.error(f"Erro ao inserir horário: {e}")
            else:
                time.sleep(1)
                st.rerun()

    @staticmethod
    def confirmar():
        st.header("Confirmar Horários")

        horarios = []
        for horario in View.horario_listar_profissional(st.session_state["usuario_id"]):
            if not horario.get_confirmado() and horario.get_idcliente() is not None:
                horarios.append(horario)

        if len(horarios) == 0:
            st.write("Nenhum horário para confirmar.")
        else:
            op = st.selectbox(
                "Atualização de Horários", horarios, format_func=lambda x: str(x)
            )
            if op is not None:
                op = View.horario_listar_id(op.get_id())

                clientes = View.cliente_listar()
                cliente_index = next(
                    (
                        i
                        for i, c in enumerate(clientes)
                        if c.get_id() == op.get_idcliente()
                    ),
                    0,
                )
                cliente = st.selectbox(
                    "Selecione o cliente",
                    clientes,
                    index=cliente_index,
                    format_func=lambda x: str(x),
                    key=f"cliente_{op.get_id()}",
                    disabled=True,
                )

                if st.button("Confirmar", key=f"btn_atualizar_{op.get_id()}"):
                    try:
                        View.horario_atualizar(
                            op.get_id(),
                            True,
                            op.get_datahora(),
                            cliente.get_id(),
                            op.get_idservico(),
                            op.get_idprofissional(),
                        )
                    except ValueError as e:
                        st.error(f"Erro ao atualizar o horário: {e}")
                    else:
                        st.success("Horário atualizado com sucesso")
                        time.sleep(1)
                        st.rerun()
