from views import View
import re
from datetime import datetime

class UI:
    @staticmethod    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            match op:
                case 1: UI.inserir()
                case 2: UI.listar()
                case 3: UI.listar_id()
                case 4: UI.atualizar()
                case 5: UI.deletar()
                case 6: UI.buscar_iniciais()
                case 7: UI.aniversariantes()

    @staticmethod
    def menu():
        op = input(
            "\nInforme uma opção:\n 1: Inserir,\n 2: Listar,\n 3: Buscar por ID,\n 4: Atualizar,\n 5: Deletar,\n 6: Buscar por iniciais,\n 7: Listar aniversariantes,\n 9: Sair\nInforme sua opção: "
        )
        if op.isdigit():
            return int(op)
        return 0
    
    @staticmethod    
    def inserir():
        nome = input("Informe o nome do contato: ")
        telefone = input("Informe o telefone: ")
        email = input("Informe o email: ")
        nascimento = UI.validar_data("Informe o nascimento (dd/mm/aaaa): ")
        View.contato_inserir(nome, telefone, email, nascimento)
        print("Contato inserido com sucesso")

    @staticmethod
    def formatar_telefone(telefone):
        # Remove tudo que não é dígito
        telefone = re.sub(r'\D', '', telefone)
        if len(telefone) == 11:
            # (XX) 9XXXX-XXXX
            return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        elif len(telefone) == 10:
            # (XX) XXXX-XXXX
            return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
        else:
            return telefone

    @staticmethod
    def listar():
        for cliente in View.contato_listar():
            print(
                f"ID: {cliente.id} - Nome: {cliente.nome} - Telefone: {UI.formatar_telefone(cliente.telefone)} - Email: {cliente.email} - Nascimento: {cliente.nascimento.strftime('%d/%m/%Y')}"
            )
    
    @staticmethod
    def listar_id():
        id = UI.validar_id("Informe o ID do contato: ")
        for cliente in View.contato_listar():
            if cliente.id == id:
                print(
                    f"ID: {cliente.id} - Nome: {cliente.nome} - Telefone: {UI.formatar_telefone(cliente.telefone)} - Email: {cliente.email} - Nascimento: {cliente.nascimento.strftime('%d/%m/%Y')}"
                )
                return
        print("Cliente não encontrado")
    
    @staticmethod
    def atualizar():
        id = UI.validar_id("Informe o ID do contato: ")
        for cliente in View.contato_listar():
            if cliente.id == id:
                print(cliente)
                op = input("Atualizar:\n 1: Nome,\n 2: Telefone,\n 3: Email,\n 4: Nascimento.\nInforme os números das opções que deseja modificar : ")
                nome, fone, email, nascimento = None, None, None, None
                if '1' in op: nome = input("Informe o novo nome do cliente: ")
                if '2' in op: fone = input("Informe o novo telefone do cliente: ")
                if '3' in op: email = input("Informe o novo email do cliente: ")
                if '4' in op: nascimento = UI.validar_data("Informe o novo nascimento (dd/mm/aaaa): ")
                if View.contato_atualizar(id, nome, fone, email, nascimento):
                    print("Cliente atualizado com sucesso!")
                else:
                    print("Erro ao atualizar contato.")

    @staticmethod
    def deletar():
        id = UI.validar_id("Informe o ID do contato a ser deletado: ")
        print("Contato deletado com sucesso" if View.contato_deletar(id) else "Erro ao deletar contato")

    @staticmethod
    def buscar_iniciais():
        iniciais = input("Informe a inicial do nome a ser buscadas: ").strip().lower()
        for cliente in View.contato_listar():
            if cliente.nome.lower().startswith(iniciais):
                print(cliente)
        if not any(cliente.nome.lower().startswith(iniciais) for cliente in View.contato_listar()):
            print("Nenhum contato encontrado com essas iniciais.")

    @staticmethod
    def aniversariantes():
        mes = UI.validar_mes("Informe o mês (1-12) para listar aniversariantes: ")
        meses = {
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
            7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        }
        print(f"Aniversariantes de {meses[mes]} ({mes}):")
        for cliente in View.contato_listar():
            if cliente.nascimento.month == mes:
                print(f"ID: {cliente.id}, Nome: {cliente.nome}, Nascimento: {cliente.nascimento.strftime('%d/%m/%Y')}")
        if not any(cliente.nascimento.month == mes for cliente in View.contato_listar()):
            print(f"Nenhum aniversariante encontrado para {meses[mes]}.")

    @staticmethod
    def validar_id(msg):
        while True:
            valor = input(msg)
            if valor.isdigit():
                return int(valor)
            print("ID inválido. Digite um número inteiro.")

    @staticmethod
    def validar_data(msg):
        while True:
            valor = input(msg)
            try:
                datetime.strptime(valor, "%d/%m/%Y")
                return valor
            except ValueError:
                print("Data inválida. Use o formato dd/mm/aaaa.")

    @staticmethod
    def validar_mes(msg):
        while True:
            valor = input(msg)
            if valor.isdigit() and 1 <= int(valor) <= 12:
                return int(valor)
            print("Mês inválido. Digite um número entre 1 e 12.")

if __name__ == "__main__":
    UI.main()
