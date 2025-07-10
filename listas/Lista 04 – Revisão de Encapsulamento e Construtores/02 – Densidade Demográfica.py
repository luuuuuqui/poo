class País:
    def __init__(self):
        self.__nome = ''
        self.__população = 0
        self.__área = 0.0

    def set_nome(self, v):
        if isinstance(v, str) and v.split():
            self.__nome = v
        else: raise ValueError('O nome do país não pode ser vazio.')
    
    def get_nome(self):
        return self.__nome
    
    def set_população(self, v):
        if isinstance(v, int) and v > 0:
            self.__população = v
        else: raise ValueError('A populção não pode ser negativa ou igual a zero.')
    
    def get_população(self):
        return self.__população

    def set_área(self, v):
        if isinstance(v, float) and v > 0:
            self.__área = v
        else: raise ValueError('A área não pode ser negativa ou igual a zero.')
    
    def get_área(self):
        return self.__área
    
    def calc_densidade(self):
        return self.__população / self.__área

class PaísUI:
    @staticmethod
    def menu():
        op = input('\nInforme uma opção:\n  1: Densidade Demográfica,\n  2: Fim.\nOpção selecionada: ')
        if op.isdigit(): return int(op)
        else: return 0
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = PaísUI.menu()
            match op:
                case 1: PaísUI.cálculo()
    @staticmethod
    def cálculo():
        p = País()
        p.set_nome(input('Digite o nome do país: '))
        p.set_população(int(input('Digite a quantidade de habitantes: ')))
        p.set_área(float(input('Digite a área do país: ')))

        print(f'\nDados de um país:')
        print(f'  Nome: {p.get_nome()}.')
        print(f'  População: {p.get_população()}')
        print(f'  Área: {p.get_área()}km².')
        print(f'  Densidade: {p.calc_densidade()}hab/km².')

UI = PaísUI()
UI.main()