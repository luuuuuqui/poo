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

class Frete:
    def __init__(self):
        self.__distancia = 0.0
        self.__peso = 0.0

class EquaçãoQuadrática:
    def __init__(self):
        self.set_a(0)
        self.set_b(0)
        self.set_c(0)

    def set_a(self, v):
        self.__a = v

    def get_a(self):
        return self.__a
    
    def set_b(self, v):
        self.__b = v

    def get_b(self):
        return self.__b
    
    def set_c(self, v):
        self.__c = v

    def get_c(self):
        return self.__c

    def calc_delta(self):
        self.__delta = self.__b ** 2 - 4 * self.__a * self.__c
        return self.__delta
    
    def is_root_real(self):
        if self.calc_delta() < 0: return False
        return True
    
    def calc_root1(self):
        return (-self.__b + self.calc_delta() ** 0.5) / (2 * self.__a)

    def calc_root2(self):
        return (-self.__b - self.calc_delta() ** 0.5) / (2 * self.__a)

class UI:
    @staticmethod
    def menu():
        op = input('\nInforme uma opção:\n  1: Retângulo,\n  2: Frete \x1b[3m(não disponível no momento)\x1b[0m.\n  3: Equação quadrática,\n  9: Fim.\nOpção selecionada: ')
        if op.isdigit(): return int(op)
        else: return 0
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            match op:
                case 1: UI.retangulo()
                case 2: UI.frete()
                case 3: UI.eq_quadratica()
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
    @staticmethod
    def frete():
        # tem que fazer o código do frete, paizão.
        pass
    @staticmethod
    def eq_quadratica():
        eq = EquaçãoQuadrática()
        print('\nEquação: Quadrática (ax² + bx + c)')
        eq.set_a(float(input('  Informe o valor de a: ')))
        eq.set_b(float(input('  Informe o valor de b: ')))
        eq.set_c(float(input('  Informe o valor de c: ')))

        print(f'\nEquação: {eq.get_a()}x² + {eq.get_b()}x + {eq.get_c()}')
        print(f'  Delta: {eq.calc_delta()}')
        print(f'  Tem raízes reais? {'Sim' if eq.is_root_real() else 'Não'}.')
        print(f'  Raiz 1: {eq.calc_root1()}')
        print(f'  Raiz 2: {eq.calc_root2()}')

UI.main()