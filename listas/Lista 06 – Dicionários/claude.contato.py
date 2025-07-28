import json
import os
from datetime import datetime

class Contato:
    """
    Classe que representa um contato individual na agenda.
    Cada contato possui identificador único, nome, email, telefone e data de nascimento.
    """
    
    def __init__(self, id, nome, email, telefone, data_nascimento):
        """
        Construtor da classe Contato.
        Inicializa um novo contato com os dados fornecidos.
        
        Args:
            id (int): Identificador único do contato
            nome (str): Nome completo do contato
            email (str): Endereço de email do contato
            telefone (str): Número de telefone do contato
            data_nascimento (str): Data de nascimento no formato DD/MM/AAAA
        """
        self._id = id
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._data_nascimento = data_nascimento
    
    # Métodos de acesso (getters) - permitem recuperar os dados do contato
    def get_id(self):
        """Retorna o ID do contato"""
        return self._id
    
    def get_nome(self):
        """Retorna o nome do contato"""
        return self._nome
    
    def get_email(self):
        """Retorna o email do contato"""
        return self._email
    
    def get_telefone(self):
        """Retorna o telefone do contato"""
        return self._telefone
    
    def get_data_nascimento(self):
        """Retorna a data de nascimento do contato"""
        return self._data_nascimento
    
    # Métodos modificadores (setters) - permitem alterar os dados do contato
    def set_nome(self, nome):
        """Altera o nome do contato"""
        self._nome = nome
    
    def set_email(self, email):
        """Altera o email do contato"""
        self._email = email
    
    def set_telefone(self, telefone):
        """Altera o telefone do contato"""
        self._telefone = telefone
    
    def set_data_nascimento(self, data_nascimento):
        """Altera a data de nascimento do contato"""
        self._data_nascimento = data_nascimento
    
    def to_string(self):
        """
        Método ToString que retorna uma representação textual completa do contato.
        Formata todas as informações do contato de forma organizada.
        
        Returns:
            str: String formatada com todos os dados do contato
        """
        return f"ID: {self._id} | Nome: {self._nome} | Email: {self._email} | Telefone: {self._telefone} | Nascimento: {self._data_nascimento}"
    
    def to_dict(self):
        """
        Converte o contato para um dicionário Python.
        Útil para salvar os dados em arquivo JSON.
        
        Returns:
            dict: Dicionário com os dados do contato
        """
        return {
            'id': self._id,
            'nome': self._nome,
            'email': self._email,
            'telefone': self._telefone,
            'data_nascimento': self._data_nascimento
        }
    
    @staticmethod
    def from_dict(data):
        """
        Cria um objeto Contato a partir de um dicionário.
        Método estático usado para carregar contatos do arquivo.
        
        Args:
            data (dict): Dicionário com os dados do contato
            
        Returns:
            Contato: Nova instância de Contato
        """
        return Contato(data['id'], data['nome'], data['email'], data['telefone'], data['data_nascimento'])


class ContatoUI:
    """
    Classe responsável pela interface do usuário e gerenciamento da lista de contatos.
    Implementa todas as operações de CRUD (Create, Read, Update, Delete) e funcionalidades extras.
    """
    
    def __init__(self):
        """
        Construtor da interface do usuário.
        Inicializa uma lista vazia de contatos e define o próximo ID disponível.
        """
        self.contatos = []  # Lista que armazenará todos os contatos
        self.proximo_id = 1  # Controla o próximo ID a ser atribuído
    
    def main(self):
        """
        Método principal que inicia a aplicação.
        Executa um loop infinito mostrando o menu até que o usuário escolha sair.
        """
        print("=== SISTEMA DE CADASTRO DE CONTATOS ===")
        print("Bem-vindo ao seu gerenciador de agenda!")
        
        while True:
            opcao = self.menu()
            
            # Estrutura de controle que direciona para a função apropriada
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.listar()
            elif opcao == '3':
                self.listar_id()
            elif opcao == '4':
                self.atualizar()
            elif opcao == '5':
                self.excluir()
            elif opcao == '6':
                self.pesquisar()
            elif opcao == '7':
                self.aniversariantes()
            elif opcao == '8':
                self.abrir()
            elif opcao == '9':
                self.salvar()
            elif opcao == '0':
                print("Obrigado por usar o sistema! Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")
            
            # Pausa para o usuário ver o resultado antes de mostrar o menu novamente
            input("\nPressione Enter para continuar...")
    
    def menu(self):
        """
        Exibe o menu de opções para o usuário.
        Apresenta todas as funcionalidades disponíveis de forma organizada.
        
        Returns:
            str: Opção escolhida pelo usuário
        """
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("="*50)
        print("1. Inserir novo contato")
        print("2. Listar todos os contatos")
        print("3. Buscar contato por ID")
        print("4. Atualizar dados de um contato")
        print("5. Excluir contato")
        print("6. Pesquisar por iniciais do nome")
        print("7. Listar aniversariantes do mês")
        print("8. Abrir contatos de arquivo")
        print("9. Salvar contatos em arquivo")
        print("0. Sair")
        print("="*50)
        
        return input("Escolha uma opção: ").strip()
    
    def inserir(self):
        """
        Solicita os dados de um novo contato ao usuário e o adiciona à lista.
        Valida os dados de entrada e garante que o ID seja único.
        """
        print("\n--- INSERIR NOVO CONTATO ---")
        
        try:
            # Coleta os dados do usuário com validação básica
            nome = input("Nome completo: ").strip()
            if not nome:
                print("Nome não pode estar vazio!")
                return
            
            email = input("Email: ").strip()
            if not email:
                print("Email não pode estar vazio!")
                return
            
            telefone = input("Telefone: ").strip()
            if not telefone:
                print("Telefone não pode estar vazio!")
                return
            
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
            if not self._validar_data(data_nascimento):
                print("Data inválida! Use o formato DD/MM/AAAA")
                return
            
            # Cria o novo contato com ID automático
            novo_contato = Contato(self.proximo_id, nome, email, telefone, data_nascimento)
            self.contatos.append(novo_contato)
            self.proximo_id += 1
            
            print(f"Contato '{nome}' inserido com sucesso! ID: {novo_contato.get_id()}")
            
        except Exception as e:
            print(f"Erro ao inserir contato: {e}")
    
    def listar(self):
        """
        Exibe todos os contatos cadastrados na agenda.
        Mostra uma mensagem apropriada se não houver contatos.
        """
        print("\n--- LISTA DE TODOS OS CONTATOS ---")
        
        if not self.contatos:
            print("Nenhum contato cadastrado ainda.")
            return
        
        print(f"Total de contatos: {len(self.contatos)}")
        print("-" * 80)
        
        # Itera sobre todos os contatos e os exibe formatados
        for contato in self.contatos:
            print(contato.to_string())
    
    def listar_id(self):
        """
        Busca e exibe um contato específico pelo seu ID.
        Solicita o ID ao usuário e mostra o contato correspondente.
        """
        print("\n--- BUSCAR CONTATO POR ID ---")
        
        try:
            id_busca = int(input("Digite o ID do contato: "))
            
            # Procura o contato na lista pelo ID
            contato_encontrado = self._buscar_por_id(id_busca)
            
            if contato_encontrado:
                print("\nContato encontrado:")
                print("-" * 50)
                print(contato_encontrado.to_string())
            else:
                print(f"Contato com ID {id_busca} não encontrado.")
                
        except ValueError:
            print("ID deve ser um número inteiro!")
    
    def atualizar(self):
        """
        Permite atualizar os dados de um contato existente.
        O usuário escolhe qual campo deseja modificar.
        """
        print("\n--- ATUALIZAR CONTATO ---")
        
        try:
            id_busca = int(input("Digite o ID do contato a ser atualizado: "))
            contato = self._buscar_por_id(id_busca)
            
            if not contato:
                print(f"Contato com ID {id_busca} não encontrado.")
                return
            
            print(f"\nContato atual: {contato.to_string()}")
            print("\nO que deseja atualizar?")
            print("1. Nome")
            print("2. Email")  
            print("3. Telefone")
            print("4. Data de nascimento")
            
            opcao = input("Escolha uma opção: ").strip()
            
            # Atualiza o campo escolhido pelo usuário
            if opcao == '1':
                novo_nome = input("Novo nome: ").strip()
                if novo_nome:
                    contato.set_nome(novo_nome)
                    print("Nome atualizado com sucesso!")
                    
            elif opcao == '2':
                novo_email = input("Novo email: ").strip()
                if novo_email:
                    contato.set_email(novo_email)
                    print("Email atualizado com sucesso!")
                    
            elif opcao == '3':
                novo_telefone = input("Novo telefone: ").strip()
                if novo_telefone:
                    contato.set_telefone(novo_telefone)
                    print("Telefone atualizado com sucesso!")
                    
            elif opcao == '4':
                nova_data = input("Nova data de nascimento (DD/MM/AAAA): ").strip()
                if self._validar_data(nova_data):
                    contato.set_data_nascimento(nova_data)
                    print("Data de nascimento atualizada com sucesso!")
                else:
                    print("Data inválida!")
            else:
                print("Opção inválida!")
                
        except ValueError:
            print("ID deve ser um número inteiro!")
    
    def excluir(self):
        """
        Remove um contato da agenda pelo seu ID.
        Pede confirmação antes de realizar a exclusão.
        """
        print("\n--- EXCLUIR CONTATO ---")
        
        try:
            id_busca = int(input("Digite o ID do contato a ser excluído: "))
            contato = self._buscar_por_id(id_busca)
            
            if not contato:
                print(f"Contato com ID {id_busca} não encontrado.")
                return
            
            print(f"\nContato a ser excluído: {contato.to_string()}")
            confirmacao = input("Tem certeza que deseja excluir? (s/n): ").strip().lower()
            
            if confirmacao == 's':
                # Remove o contato da lista
                self.contatos.remove(contato)
                print("Contato excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
                
        except ValueError:
            print("ID deve ser um número inteiro!")
    
    def pesquisar(self):
        """
        Busca contatos cujo nome começa com as iniciais fornecidas pelo usuário.
        Realiza busca case-insensitive (não diferencia maiúsculas de minúsculas).
        """
        print("\n--- PESQUISAR POR INICIAIS ---")
        
        iniciais = input("Digite as iniciais do nome: ").strip().lower()
        if not iniciais:
            print("Iniciais não podem estar vazias!")
            return
        
        contatos_encontrados = []
        
        # Busca todos os contatos que começam com as iniciais
        for contato in self.contatos:
            if contato.get_nome().lower().startswith(iniciais):
                contatos_encontrados.append(contato)
        
        if contatos_encontrados:
            print(f"\nEncontrados {len(contatos_encontrados)} contato(s):")
            print("-" * 80)
            for contato in contatos_encontrados:
                print(contato.to_string())
        else:
            print(f"Nenhum contato encontrado com iniciais '{iniciais}'.")
    
    def aniversariantes(self):
        """
        Lista todos os contatos que fazem aniversário em um mês específico.
        O usuário informa o número do mês (1-12).
        """
        print("\n--- ANIVERSARIANTES DO MÊS ---")
        
        try:
            mes = int(input("Digite o número do mês (1-12): "))
            
            if mes < 1 or mes > 12:
                print("Mês deve estar entre 1 e 12!")
                return
            
            aniversariantes = []
            
            # Procura contatos que aniversariam no mês informado
            for contato in self.contatos:
                try:
                    # Extrai o mês da data de nascimento (formato DD/MM/AAAA)
                    data_parts = contato.get_data_nascimento().split('/')
                    if len(data_parts) == 3:
                        mes_nascimento = int(data_parts[1])
                        if mes_nascimento == mes:
                            aniversariantes.append(contato)
                except:
                    continue  # Ignora datas com formato inválido
            
            # Nomes dos meses para exibição mais amigável
            nomes_meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                          "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
            
            if aniversariantes:
                print(f"\nAniversariantes de {nomes_meses[mes]}:")
                print("-" * 80)
                for contato in aniversariantes:
                    print(contato.to_string())
            else:
                print(f"Nenhum aniversariante encontrado para {nomes_meses[mes]}.")
                
        except ValueError:
            print("Mês deve ser um número inteiro!")
    
    def abrir(self):
        """
        Carrega a lista de contatos de um arquivo JSON.
        Substitui a lista atual pelos dados do arquivo.
        """
        print("\n--- ABRIR ARQUIVO DE CONTATOS ---")
        
        nome_arquivo = input("Nome do arquivo (sem extensão): ").strip()
        if not nome_arquivo:
            nome_arquivo = "contatos"
        
        nome_arquivo += ".json"
        
        try:
            # Verifica se o arquivo existe
            if not os.path.exists(nome_arquivo):
                print(f"Arquivo '{nome_arquivo}' não encontrado!")
                return
            
            # Lê o arquivo JSON
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            
            # Converte os dados para objetos Contato
            self.contatos = []
            for item in dados['contatos']:
                contato = Contato.from_dict(item)
                self.contatos.append(contato)
            
            # Atualiza o próximo ID disponível
            if self.contatos:
                self.proximo_id = max(contato.get_id() for contato in self.contatos) + 1
            else:
                self.proximo_id = 1
            
            print(f"Arquivo '{nome_arquivo}' carregado com sucesso!")
            print(f"Total de contatos carregados: {len(self.contatos)}")
            
        except json.JSONDecodeError:
            print("Erro: Arquivo não está em formato JSON válido!")
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")
    
    def salvar(self):
        """
        Salva a lista atual de contatos em um arquivo JSON.
        Permite ao usuário escolher o nome do arquivo.
        """
        print("\n--- SALVAR CONTATOS EM ARQUIVO ---")
        
        if not self.contatos:
            print("Nenhum contato para salvar!")
            return
        
        nome_arquivo = input("Nome do arquivo (sem extensão): ").strip()
        if not nome_arquivo:
            nome_arquivo = "contatos"
        
        nome_arquivo += ".json"
        
        try:
            # Converte os contatos para formato de dicionário
            dados = {
                'contatos': [contato.to_dict() for contato in self.contatos],
                'data_salvamento': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }
            
            # Salva no arquivo JSON com formatação bonita
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=2, ensure_ascii=False)
            
            print(f"Contatos salvos com sucesso no arquivo '{nome_arquivo}'!")
            print(f"Total de contatos salvos: {len(self.contatos)}")
            
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def _buscar_por_id(self, id_busca):
        """
        Método auxiliar privado para buscar um contato pelo ID.
        
        Args:
            id_busca (int): ID do contato a ser buscado
            
        Returns:
            Contato: Objeto contato encontrado ou None se não encontrado
        """
        for contato in self.contatos:
            if contato.get_id() == id_busca:
                return contato
        return None
    
    def _validar_data(self, data):
        """
        Método auxiliar privado para validar o formato da data.
        
        Args:
            data (str): Data no formato DD/MM/AAAA
            
        Returns:
            bool: True se a data é válida, False caso contrário
        """
        try:
            # Tenta criar um objeto datetime para validar a data
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False


# Ponto de entrada do programa
if __name__ == "__main__":
    # Cria uma instância da interface do usuário e inicia a aplicação
    app = ContatoUI()
    app.main()