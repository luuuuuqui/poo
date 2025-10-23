
## Estrutura principal
- [Poo13/index.py](Poo13/index.py) — Interface principal do Streamlit (`IndexUI.main`)  
  - Classe: [`IndexUI.main`](Poo13/index.py)
- [Poo13/views.py](Poo13/views.py) — Camada de *business logic* / integração entre UI e modelos  
  - Exemplos de métodos: [`View.autenticar`](Poo13/views.py), [`View.cliente_inserir`](Poo13/views.py)
- Modelos (persistência em JSON)
  - [Poo13/models/cliente.py](Poo13/models/cliente.py) — Classe `Cliente` (`Cliente.__init__`, `Cliente.to_json`)  
 - Referência: [`Cliente.__init__`](Poo13/models/cliente.py), [`Cliente.to_json`](Poo13/models/cliente.py)
  - [Poo13/models/servico.py](Poo13/models/servico.py) — `Servico` e `ServicoDAO` (`Servico.to_json`, `ServicoDAO.salvar`)  
 - Referência: [`Servico.to_json`](Poo13/models/servico.py), [`ServicoDAO.salvar`](Poo13/models/servico.py)
  - [Poo13/models/profissional.py](Poo13/models/profissional.py) — `Profissional` (`Profissional.to_json`)
 - Referência: [`Profissional.to_json`](Poo13/models/profissional.py)
- UIs (Streamlit)
  - [Poo13/templates/manterclienteUI.py](Poo13/templates/manterclienteUI.py) — [`ManterClienteUI.main`](Poo13/templates/manterclienteUI.py)
  - [Poo13/templates/manterservicoUI.py](Poo13/templates/manterservicoUI.py) — [`ManterServicoUI.main`](Poo13/templates/manterservicoUI.py)
  - [Poo13/templates/manterprofissionalUI.py](Poo13/templates/manterprofissionalUI.py) — [`ManterProfissionalUI.main`](Poo13/templates/manterprofissionalUI.py)
  - [Poo13/templates/manterhorarioUI.py](Poo13/templates/manterhorarioUI.py) — [`ManterHorarioUI.main`](Poo13/templates/manterhorarioUI.py)
  - [Poo13/templates/loginUI.py](Poo13/templates/loginUI.py) — [`LoginUI.main`](Poo13/templates/loginUI.py)
  - [Poo13/templates/abrircontaUI.py](Poo13/templates/abrircontaUI.py) — [`AbrirContaUI.main`](Poo13/templates/abrircontaUI.py)
  - [Poo13/templates/perfilclienteUI.py](Poo13/templates/perfilclienteUI.py) — [`PerfilClienteUI.main`](Poo13/templates/perfilclienteUI.py)
  - [Poo13/templates/perfilprofissionalUI.py](Poo13/templates/perfilprofissionalUI.py) — [`PerfilProfissionalUI.main`](Poo13/templates/perfilprofissionalUI.py)
  - [Poo13/templates/agendarservicoUI.py](Poo13/templates/agendarservicoUI.py) — [`AgendarServicoUI.main`](Poo13/templates/agendarservicoUI.py)

## Outros pontos de interesse
- App de demonstração Streamlit: [Streamlit/index.py](Streamlit/index.py) (exibe textos em [Streamlit/beemovie.txt](Streamlit/beemovie.txt) e [Streamlit/bark.txt](Streamlit/bark.txt))
- Exercícios e listas do semestre: diretório `.primeiro semestre/` (várias atividades e exemplos)
- Arquivos de dados persistidos (JSON): [Poo13/clientes.json](Poo13/clientes.json), [Poo13/servicos.json](Poo13/servicos.json), [Poo13/profissionais.json](Poo13/profissionais.json), [Poo13/horarios.json](Poo13/horarios.json)

## Dicas rápidas de desenvolvimento
- As DAOs usam JSON para persistência. Ex.: [`ServicoDAO.abrir`](Poo13/models/servico.py) e [`ServicoDAO.salvar`](Poo13/models/servico.py).
- A autenticação passa por [`View.autenticar`](Poo13/views.py) e as UIs atualizam `st.session_state`.
- Para adicionar novos campos aos modelos, atualize `to_json`/`from_json` em cada model.

Se quiser, atualizo esse README com instruções de testing, CI ou um guia de contribuição.