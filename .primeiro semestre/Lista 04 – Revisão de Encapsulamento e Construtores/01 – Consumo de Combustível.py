class Viagem:
    def __init__(self):
        self.__destino = ''
        self.__distancia = 0.0
        self.__litros = 0.0

    def set_destino(self, destino):
        if isinstance(destino, str) and destino.strip():
            self.__destino = destino
        else: raise ValueError('O destino não pode ser vazio.')
    
    def get_destino(self):
        return self.__destino
    
    def set_distancia(self, distancia):
        if isinstance(distancia, (int, float)) and distancia > 0:
            self.__distancia = distancia
        else: raise ValueError('A distância deve ser um número positivo.')

    def get_distancia(self):
        return self.__distancia
    
    def set_litros(self, litros):
        if isinstance(litros, (int, float)) and litros > 0:
            self.__litros = litros
        else: raise ValueError('Os litros devem ser um número positivo.')
    
    def get_litros(self):
        return self.__litros

    def calc_consumo(self):
        return self.__distancia / self.__litros


class ViagemUI:
    @staticmethod
    def menu():
        op = int(input('\nInforme uma opção:\n  1: Consumo de combustível,\n  9: Fim.\nOpção selecionada: '))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
    @staticmethod
    def calculo():
        v = Viagem

        v.set_destino(str(input('Digite o destino: ')))
        v.set_distancia(int(input('Digite a distância em km: ')))
        v.set_litros(input(int('Digite o combustível gasto: ')))


        print(f'Dados da viagem:')
        print(f'  Destino: {v.get_destino}.')
        print(f'  Distância do ponto de partida: {v.get_distancia}km')
        print(f'  Combustível gasto: {v.get_litros}L')
        print(f'  Consumo médio: {v.calc_consumo}km/L')
        

UI = ViagemUI
UI.main()