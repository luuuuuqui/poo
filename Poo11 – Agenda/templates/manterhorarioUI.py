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
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            clientes = {c.get_id(): c.get_nome() for c in View.cliente_listar()}
            servicos = {s.get_id(): s.get_descricao() for s in View.servico_listar()}
            profissionais = {p.get_id(): p.get_nome() for p in View.profissional_listar()}
            for obj in horarios:
                dic = {
                    "id": obj.get_id(),
                    "confirmado": obj.get_confirmado(),
                    "datahora": obj.get_datahora().strftime("%d/%m/%Y %H:%M") if obj.get_datahora() else "",
                    "cliente": clientes.get(obj.get_idcliente(), obj.get_idcliente()),
                    "servico": servicos.get(obj.get_idservico(), obj.get_idservico()),
                    "profissional": profissionais.get(obj.get_idprofissional(), obj.get_idprofissional())
                }
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def inserir():
        confirmado = st.checkbox("Confirmado")
        d = st.date_input("Dia do atendimento:", value=None, format="DD/MM/YYYY")
        t = st.time_input("Horário do atendimento:", value=None)
        datahora = None

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
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Atualização de Horários", horarios, format_func=lambda x: str(x))
            if op is not None:
                confirmado = st.checkbox(
                    "Confirmado", 
                    value=op.get_confirmado(), 
                    key=f"confirmado_{op.get_id()}"
                )
                d = st.date_input(
                    "Dia do atendimento:", 
                    value=op.get_datahora().date() if op.get_datahora() else None, 
                    key=f"data_{op.get_id()}", format="DD/MM/YYYY"
                )
                t = st.time_input(
                    "Horário do atendimento:", 
                    value=op.get_datahora().time() if op.get_datahora() else None, 
                    key=f"hora_{op.get_id()}"
                )
                datahora = None
                if d is not None and t is not None:
                    datahora = datetime.datetime(d.year, d.month, d.day, t.hour, t.minute, t.second)
                clientes = View.cliente_listar()
                cliente = st.selectbox(
                    "Selecione o cliente", clientes, 
                    index=[i for i, c in enumerate(clientes) if c.get_id() == op.get_idcliente()][0] if clientes else 0, 
                    format_func=lambda x: str(x),
                    key=f"cliente_{op.get_id()}"
                )
                servicos = View.servico_listar()
                servico = st.selectbox(
                    "Selecione o serviço", servicos, 
                    index=[i for i, s in enumerate(servicos) if s.get_id() == op.get_idservico()][0] if servicos else 0, 
                    format_func=lambda x: str(x),
                    key=f"servico_{op.get_id()}"
                )
                profissionais = View.profissional_listar()
                profissional = st.selectbox(
                    "Selecione o profissional", profissionais, 
                    index=[i for i, p in enumerate(profissionais) if p.get_id() == op.get_idprofissional()][0] if profissionais else 0, 
                    format_func=lambda x: str(x),
                    key=f"profissional_{op.get_id()}"
                )

                if not datahora or not cliente or not servico or not profissional:
                    st.warning("Preencha todos os campos")
                
                elif st.button("Atualizar", key=f"btn_atualizar_{op.get_id()}"):
                    View.horario_atualizar(op.get_id(), confirmado, datahora, cliente.get_id(), servico.get_id(), profissional.get_id())
                    st.success("Horário atualizado com sucesso")
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
