'''
3. Uma Agenda de Contatos

Escreva a classe Contato de acordo com o diagrama UML apresentado. A classe é utilizada para representar os

contatos da agenda:

• Cada contato da agenda deve possuir um identificador (id), nome, e-mail, telefone e data de nascimento;

• O método Contato é um construtor que recebe os dados iniciais de um contato;

• O método ToString retorna um texto contendo todas as informações de um contato;

• Inclua métodos de acesso na classe para permitir alterar e recuperar os dados de um contato (não apresentados

no diagrama.

Escreva a classe ContatoUI, de acordo com o diagrama, para manter uma lista de contato e realizar as seguintes

operações:

• Main inicia a aplicação mostrando um menu de opções em loop, até que a opção “Sair” seja selecionada;

• Menu deve mostrar as opções do usuário: inserir um novo contato na agenda, listar todos os contatos, atualizar

os dados de um contato, excluir um contato da agenda, pesquisar um contato cadastrado pelas iniciais do nome

e sair;

• Inserir solicita os dados de um contato do usuário, instancia um novo contato e insere na lista;

• Listar mostra todos os contatos cadastrados;

• Atualizar atualiza os dados de um contato;

• Excluir remove um contato da lista;

• Pesquisar procura um contato na lista de acordo com as iniciais fornecidas pelo usuário;

• Aniversariantes mostra os contatos na agenda que aniversariam em um mês informado pelo usuário.
'''

import datetime

class Contato:
    def __init__(self, id, nome, email, telefone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)
    
    def set_id(self, id):
        if isinstance(id, int) and id > 0:
            self.__id = id
        else:
            raise ValueError("ID inválido. Deve ser um número inteiro positivo.")
    
    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome.strip()
        else:
            raise ValueError("Nome inválido. Deve ser uma string não vazia.")
    
    def get_nome(self):
        return self.__nome
    
    def set_email(self, email):
        if isinstance(email, str) and '@' in email and '.' in email:
            self.__email = email.strip()
        else:
            raise ValueError("Email inválido. Deve conter @ e .")
    
    def get_email(self):
        return self.__email
    
    def set_telefone(self, telefone):
        if isinstance(telefone, str) and len(telefone) >= 10 and telefone.isdigit():
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido. Deve ser uma string de pelo menos 10 dígitos.")
    
    def get_telefone(self):
        return self.__telefone
    
    def set_nascimento(self, nascimento):
        try:
            dia, mes, ano = map(int, nascimento.split())
            self.__nascimento = datetime.date(ano, mes, dia)
        except ValueError:
            raise ValueError("Data de nascimento inválida. Deve ser no formato 'DD MM AAAA'.")
    
    def get_nascimento(self):
        return self.__nascimento
    
    def toString(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, Email: {self.__email}, Telefone: {self.__telefone}, Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"

class ContatoUI:
    contatos = []
    proximo_id = 1
    
    @staticmethod
    def menu():
        print("\n=== AGENDA DE CONTATOS ===")
        print("1 - Inserir contato")
        print("2 - Listar contatos")
        print("3 - Atualizar contato")
        print("4 - Excluir contato")
        print("5 - Pesquisar por iniciais")
        print("6 - Aniversariantes do mês")
        print("9 - Sair")
        
        op = input("Opção selecionada: ")
        if op.isdigit():
            return int(op)
        else:
            return 0
    
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = ContatoUI.menu()
            match op:
                case 1: ContatoUI.inserir()
                case 2: ContatoUI.listar()
                case 3: ContatoUI.atualizar()
                case 4: ContatoUI.excluir()
                case 5: ContatoUI.pesquisar()
                case 6: ContatoUI.aniversariantes()
                case 9: print("Saindo...")
                case _: print("Opção inválida!")
    
    @staticmethod
    def inserir():
        print("\n=== INSERIR CONTATO ===")
        try:
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone (apenas números): ")
            nascimento = input("Data de nascimento (DD MM AAAA): ")
            
            contato = Contato(ContatoUI.proximo_id, nome, email, telefone, nascimento)
            ContatoUI.contatos.append(contato)
            ContatoUI.proximo_id += 1
            print("Contato inserido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")
    
    @staticmethod
    def listar():
        print("\n=== LISTA DE CONTATOS ===")
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in ContatoUI.contatos:
                print(contato.toString())
    
    @staticmethod
    def atualizar():
        print("\n=== ATUALIZAR CONTATO ===")
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
            return
        
        try:
            id_contato = int(input("ID do contato a ser atualizado: "))
            contato = next((c for c in ContatoUI.contatos if c.get_id() == id_contato), None)
            
            if contato:
                print(f"Contato atual: {contato.toString()}")
                nome = input("Novo nome (Enter para manter): ")
                email = input("Novo email (Enter para manter): ")
                telefone = input("Novo telefone (Enter para manter): ")
                nascimento = input("Nova data de nascimento DD MM AAAA (Enter para manter): ")
                
                if nome: contato.set_nome(nome)
                if email: contato.set_email(email)
                if telefone: contato.set_telefone(telefone)
                if nascimento: contato.set_nascimento(nascimento)
                
                print("Contato atualizado com sucesso!")
            else:
                print("Contato não encontrado.")
        except (ValueError, StopIteration) as e:
            print(f"Erro: {e}")
    
    @staticmethod
    def excluir():
        print("\n=== EXCLUIR CONTATO ===")
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
            return
        
        try:
            id_contato = int(input("ID do contato a ser excluído: "))
            contato = next((c for c in ContatoUI.contatos if c.get_id() == id_contato), None)
            
            if contato:
                ContatoUI.contatos.remove(contato)
                print("Contato excluído com sucesso!")
            else:
                print("Contato não encontrado.")
        except ValueError:
            print("ID inválido.")
    
    @staticmethod
    def pesquisar():
        print("\n=== PESQUISAR POR INICIAIS ===")
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
            return
        
        iniciais = input("Digite as iniciais do nome: ").upper()
        encontrados = []
        
        for contato in ContatoUI.contatos:
            nome_palavras = contato.get_nome().upper().split()
            iniciais_nome = ''.join([palavra[0] for palavra in nome_palavras])
            
            if iniciais_nome.startswith(iniciais):
                encontrados.append(contato)
        
        if encontrados:
            print("Contatos encontrados:")
            for contato in encontrados:
                print(contato.toString())
        else:
            print("Nenhum contato encontrado com essas iniciais.")
    
    @staticmethod
    def aniversariantes():
        print("\n=== ANIVERSARIANTES DO MÊS ===")
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
            return
        
        try:
            mes = int(input("Digite o mês (1-12): "))
            if mes < 1 or mes > 12:
                print("Mês inválido.")
                return
            
            aniversariantes = []
            for contato in ContatoUI.contatos:
                if contato.get_nascimento().month == mes:
                    aniversariantes.append(contato)
            
            if aniversariantes:
                print(f"Aniversariantes do mês {mes}:")
                for contato in aniversariantes:
                    print(f"{contato.get_nome()} - {contato.get_nascimento().strftime('%d/%m/%Y')}")
            else:
                print(f"Nenhum aniversariante encontrado no mês {mes}.")
        except ValueError:
            print("Mês inválido.")

# Execução do programa
ContatoUI.main()