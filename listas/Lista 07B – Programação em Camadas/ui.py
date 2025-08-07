from views import View

class UI:
    @staticmethod    
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()

    @staticmethod    
    def menu():
        print("1-Inserir, 2-Listar, 3-Fim")
        return int(input("Informe sua opção: "))
    
    @staticmethod    
    def inserir():
        nome = input("Informe o nome do cliente: ")
        View.contato_inserir(nome)
        print("Cliente inserido com sucesso")

    @staticmethod    
    def listar():
        for cliente in View.contato_listar():
            print(cliente)
    
    @staticmethod
    def listar_id():
        id = int(input("Informe o ID do contato: "))
        for cliente in View.contato_listar():
            if cliente.id == id:
                print(cliente)
                return
        print("Cliente não encontrado")

    @staticmethod
    def atualizar():
        id = int(input("Informe o ID do contato: "))
        for cliente in View.contato_listar():
            if cliente.id == id:
                nome = input("Informe o novo nome do cliente: ")
                cliente.nome = nome
                print("Cliente atualizado com sucesso")
                return
        print("Cliente não encontrado")
UI.main()
