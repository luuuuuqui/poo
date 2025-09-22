class Retângulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0

    def set_b(self, v):
        if isinstance(v, (float, int)) and v > 0:
            self.__b = v
        else: raise ValueError('A base não pode ser um número maior que zero.')
    
    def get_b(self):
        return self.__b
    
    def set_h(self, v):
        if isinstance(v, (float, int)) and v > 0:
            self.__h = v
        else: raise ValueError('A altura não pode ser um número maior que zero.')
    
    def get_h(self):
        return self.__h
    
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** 0.5
    
    def calc_area(self):
        return self.__b * self.__h

class UI:
    @staticmethod
    def menu():
        op = input('\nInforme uma opção:\n  1: Retângulo,\n  9: Fim.\nOpção selecionada: ')
        if op.isdigit(): return int(op)
        else: return 0
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            match op:
                case 1: UI.retangulo()

    @staticmethod
    def retangulo():
        r = Retângulo()
        print('\nRetângulo:')
        r.set_b(float(input('  Informe o valor da base: ')))
        r.set_h(float(input('  Informe o valor da altura: ')))

        print(f'\nRetângulo:')
        print(f'  Base: {r.get_b()}')
        print(f'  Altura: {r.get_h()}')
        print(f'  Área: {r.calc_area()}')
        print(f'  Diagonal: {r.calc_diagonal()}')

UI.main()