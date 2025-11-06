import streamlit as st
from views import View
import time


class AgendarServicoUI:
    @staticmethod
    def main():
        st.header("Agendar Serviço")
        profs = View.profissional_listar()

        if len(profs) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            if profissional:
                horarios = View.horario_agendar_horario(profissional.get_id())

            if not horarios:
                st.write("Nenhum horário disponível")
            else:
                horario = st.selectbox("Informe o horário", horarios)
                servicos = View.servico_listar()
                servico = st.selectbox("Informe o serviço", servicos)

                if st.button("Agendar"):
                    if horario and servico and profissional: 
                        try:
                            View.horario_atualizar(
                                horario.get_id(),
                                horario.get_confirmado(),
                                horario.get_datahora(),
                                st.session_state["usuario_id"],
                                servico.get_id(),
                                profissional.get_id(),
                            )
                        except ValueError as e:
                            st.error(f"Erro ao agendar horário: {e}")
                        else:
                            st.success("Horário agendado com sucesso")
                            time.sleep(2)
                            st.rerun()
