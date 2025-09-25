# Projeto Agenda - Programação em Camadas com POO e Streamlit

Este projeto é um exemplo de aplicação de **programação orientada a objetos (POO)** utilizando o conceito de **programação em camadas**. O objetivo é organizar o código de forma modular, facilitando manutenção, testes e evolução do sistema.

## Estrutura de Pastas

- `models/`: Contém as classes principais do domínio, como `cliente.py`, `profissional.py` e `servico.py`. Cada arquivo representa uma entidade do sistema.
- `templates/`: Interface de usuário (UI) para cada entidade, usando Streamlit para criar telas interativas.
- `views.py`: Camada de controle, responsável por conectar a interface com os modelos e gerenciar a lógica de negócio.
- Arquivos `.json`: Utilizados para armazenar dados de clientes, profissionais e serviços de forma simples.

## Programação em Camadas

O projeto está dividido em três camadas principais:

1. **Modelos (models):** Definem as estruturas de dados e regras de negócio.
2. **Visão (templates):** Interface gráfica feita com Streamlit, permitindo interação do usuário.
3. **Controle (views):** Faz a ponte entre a interface e os modelos, processando ações do usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework para criação rápida de interfaces web interativas.

## Como Executar

1. Instale as dependências necessárias (Streamlit).
2. Execute o arquivo principal da interface usando o comando:
	```bash
	streamlit run index.py
	```

## Objetivo do Projeto

Este projeto serve como base para aprender e praticar:
- Organização de código em camadas
- Uso de POO em Python
- Criação de interfaces com Streamlit
- Manipulação de dados em arquivos JSON

---

Sinta-se à vontade para explorar os arquivos e modificar o projeto para seus estudos!
