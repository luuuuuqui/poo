'''
1. Um Paciente
Escreva a classe Paciente de acordo com o diagrama UML
apresentado.
• A classe deve utilizar os atributos nome, CPF, telefone e
nascimento usados no registro de dados dos pacientes de
uma clínica;
• O construtor da classe deve receber os valores iniciais dos
dados de um paciente;
• O método Idade deve retornar um texto com a idade do paciente em anos e meses, de acordo com a sua data
de nascimento e a data atual;
• O método ToString deve retornar um texto com os atributos do objeto;
• Inclua métodos de acesso na classe para permitir alterar e recuperar os dados de um paciente (não
apresentados no diagrama);
• Faça uma UI para testar a classe Paciente.
'''


import datetime

class Paciente:
    def __init__(self):
        self.__nome = ''
        self.__cpf = ''
        self.__telefone = ''
        self.__nascimento = datetime.date(2023, 8, 11) #AAAA-MM-DD
    
    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome.strip()
        else:
            raise ValueError("Nome inválido. Deve ser uma string não vazia.")
        
    def get_nome(self):
        return self.__nome
    
    def set_cpf(self, cpf):
        if len(cpf) == 11 and cpf.isdigit():
            self.__cpf = str(cpf)
        else:
            raise ValueError("CPF inválido. Deve ser uma string de 11 dígitos.")
        
    def get_cpf(self):
        return self.__cpf
    
    def set_telefone(self, telefone):
        if isinstance(telefone, str) and len(telefone) >= 10 and telefone.isdigit():
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido. Deve ser uma string de pelo menos 10 dígitos.")
        
    def get_telefone(self):
        return self.__telefone

    def set_nascimento(self, nascimento):
        # transforma DD MM AAAA em AAAA-MM-DD
        try:
            dia, mes, ano = map(int, nascimento.split())
            self.__nascimento = datetime.date(ano, mes, dia)
        except ValueError:
            raise ValueError("Data de nascimento inválida. Deve ser no formato 'DD MM AAAA'.")

    def get_nascimento(self):
        return self.__nascimento

    def idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.__nascimento.year
        return idade if (hoje.month, hoje.day) < (self.__nascimento.month, self.__nascimento.day) else idade - 1


# dados de joao pedro kkj


class UI:
    @staticmethod
    def menu():
        op = input('\nInforme uma opção:\n  1: Paciente,\n  2: Dados do paciente,\n  9: Fim.\nOpção selecionada: ')
        if op.isdigit(): return int(op)
        else: return 0
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            match op:
                case 1: UI.paciente()
                case 2: UI.dadospaciente()
    @staticmethod
    def dadospaciente():
        p = Paciente()

        p.set_nome('João Pedro Silva de Oliveira')
        p.set_cpf('33344455566') # cpf falso :(
        p.set_nascimento('19 05 2008')
        p.set_telefone('84988431104')

        print('\nDados do Paciente:')
        print(f' Nome: {p.get_nome()}')
        print(f' CPF: {p.get_cpf()[:3]}.{p.get_cpf()[3:6]}.{p.get_cpf()[6:9]}-{p.get_cpf()[9:]}')
        print(f' Telefone: ({p.get_telefone()[:2]}) {p.get_telefone()[2:7]}-{p.get_telefone()[7:]}')
        print(f' Data de Nascimento: {p.get_nascimento().strftime("%d/%m/%Y")}')
        print(f' Idade: {p.idade()} anos')

UI.main()