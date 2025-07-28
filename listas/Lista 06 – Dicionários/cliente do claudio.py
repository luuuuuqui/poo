import json
from typing import List, Optional

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    
    # Getters
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def fone(self) -> str:
        return self.__fone
    
    # Setters
    @id.setter
    def id(self, id: int):
        self.__id = id
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @email.setter
    def email(self, email: str):
        self.__email = email
    
    @fone.setter
    def fone(self, fone: str):
        self.__fone = fone
    
    def toString(self) -> str:
        return f"ID: {self.__id}, Nome: {self.__nome}, Email: {self.__email}, Fone: {self.__fone}"
    
    def to_dict(self) -> dict:
        return {
            'id': self.__id,
            'nome': self.__nome,
            'email': self.__email,
            'fone': self.__fone
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['id'], data['nome'], data['email'], data['fone'])


class ClienteUI:
    def __init__(self):
        self.clientes: List[Cliente] = []
    
    def main(self):
        while True:
            opcao = self.menu()
            
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
                self.abrir()
            elif opcao == '7':
                self.salvar()
            elif opcao == '8':
                print("Saindo...")
                exit()
            else:
                print("Opção inválida!")
    
    def menu(self) -> str:
        print("\n" + "="*50)
        print("CADASTRO DE CLIENTES")
        print("="*50)
        print("1 - Inserir novo cliente")
        print("2 - Listar todos os clientes")
        print("3 - Listar cliente por ID")
        print("4 - Atualizar dados do cliente")
        print("5 - Excluir cliente")
        print("6 - Abrir lista de arquivo")
        print("7 - Salvar lista em arquivo")
        print("8 - Sair")
        print("="*50)
        return input("Escolha uma opção: ")
    
    def inserir(self):
        print("\n--- INSERIR NOVO CLIENTE ---")
        try:
            id = int(input("ID: "))
            
            # Verificar se ID já existe
            if self._buscar_cliente_por_id(id):
                print(f"Erro: Cliente com ID {id} já existe!")
                return
            
            nome = input("Nome: ")
            email = input("Email: ")
            fone = input("Telefone: ")
            
            cliente = Cliente(id, nome, email, fone)
            self.clientes.append(cliente)
            print("Cliente inserido com sucesso!")
            
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def listar(self):
        print("\n--- LISTA DE CLIENTES ---")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        for cliente in self.clientes:
            print(cliente.toString())
    
    def listar_id(self):
        print("\n--- BUSCAR CLIENTE POR ID ---")
        try:
            id = int(input("Digite o ID do cliente: "))
            cliente = self._buscar_cliente_por_id(id)
            
            if cliente:
                print(cliente.toString())
            else:
                print(f"Cliente com ID {id} não encontrado.")
                
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def atualizar(self):
        print("\n--- ATUALIZAR CLIENTE ---")
        try:
            id = int(input("Digite o ID do cliente a atualizar: "))
            cliente = self._buscar_cliente_por_id(id)
            
            if not cliente:
                print(f"Cliente com ID {id} não encontrado.")
                return
            
            print(f"Cliente atual: {cliente.toString()}")
            
            nome = input(f"Novo nome (atual: {cliente.nome}): ")
            email = input(f"Novo email (atual: {cliente.email}): ")
            fone = input(f"Novo telefone (atual: {cliente.fone}): ")
            
            if nome.strip():
                cliente.nome = nome
            if email.strip():
                cliente.email = email
            if fone.strip():
                cliente.fone = fone
            
            print("Cliente atualizado com sucesso!")
            
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def excluir(self):
        print("\n--- EXCLUIR CLIENTE ---")
        try:
            id = int(input("Digite o ID do cliente a excluir: "))
            cliente = self._buscar_cliente_por_id(id)
            
            if not cliente:
                print(f"Cliente com ID {id} não encontrado.")
                return
            
            print(f"Cliente a excluir: {cliente.toString()}")
            confirmacao = input("Confirma exclusão? (s/n): ").lower()
            
            if confirmacao == 's':
                self.clientes.remove(cliente)
                print("Cliente excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
                
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def abrir(self):
        print("\n--- ABRIR ARQUIVO ---")
        nome_arquivo = input("Nome do arquivo (ex: clientes.json): ")
        
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                self.clientes = [Cliente.from_dict(cliente_data) for cliente_data in dados]
                print(f"Lista carregada com sucesso! {len(self.clientes)} clientes carregados.")
                
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Arquivo com formato inválido.")
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")
    
    def salvar(self):
        print("\n--- SALVAR ARQUIVO ---")
        nome_arquivo = input("Nome do arquivo (ex: clientes.json): ")
        
        try:
            dados = [cliente.to_dict() for cliente in self.clientes]
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=2, ensure_ascii=False)
                print(f"Lista salva com sucesso! {len(self.clientes)} clientes salvos.")
                
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def _buscar_cliente_por_id(self, id: int) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None


# Executar a aplicação
if __name__ == "__main__":
    app = ClienteUI()
    app.main()