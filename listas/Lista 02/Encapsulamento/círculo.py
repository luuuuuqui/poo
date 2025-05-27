class Circulo:
    def __init__(self):
        self.__raio = 0

    def set_raio(self, v):
        if v < 0: raise ValueError('O raio não pode ser igual ou menor que zero.')
        self.__raio = v

    def get_raio(self):
        return self.__raio

    def calc_area(self):
        return 3.141592 * self.__raio ** 2

    def calc_circunferencia(self):
        return 3.141592 * self.__raio * 2

class UI:
    @staticmethod
    def menu():
        op = int(input("Informe uma opção:\n  1: Círculo,\n  9: Fim.\nOpção selecionada: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.circulo()
    @staticmethod
    def circulo():
        o = Circulo()

        o.set_raio(int(input('\nDigite o raio em metros: ')))
    
        print(f'\nInformações do círculo:\n  Raio = {o.get_raio()}m\n  Diâmetro = {o.get_raio() * 2}m\n  Circunferência = {o.calc_circunferencia()}m\n  Área = {o.calc_area()}m²\n ')

UI.main()