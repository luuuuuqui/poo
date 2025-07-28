import datetime

class Treito:
    def __init__(self):
        self.__treinos = {
            '0' : {self.__tempid, self.__tempdata, self.__tempdistancia, self.__temptempo}, 
        }
        self.__tempid = 0
        self.__tempdata = datetime.date.today()
        self.__tempdistancia = 0.0
        self.__temptempo = datetime.timedelta(seconds=0)

    def inserir(self, id, data, distancia, tempo):
        self.__treinos[id] = {self.__tempdata, self.__tempdistancia, self.__temptempo}

    def __str__(self):
        return f"ID: {self.__tempid}, Data: {self.__tempdata.strftime('%d/%m/%Y')}, Distância: {self.__tempdistancia} km, Tempo: {self.__temptempo}"

class TreinoUI:
    @staticmethod
    def menu():
        op = input('\nInforme uma opção:\n 1: \n 9: Sair.\nOpção selecionada: ')
        if op.isdigit(): return int(op)
        else: return 0

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = TreinoUI.menu()
            match op:
                case 1: TreinoUI.inserir()
                case 2: TreinoUI.listar()
                case 3: TreinoUI.listar_id()
                case 4: TreinoUI.atualizar()
                case 5: TreinoUI.excluir()
                case 6: TreinoUI.maisRapido()

    @staticmethod
    def inserir():
        if 
        pass

    @staticmethod
    def listar():
        # listar todos os treinos do atleta
        pass
    
    @staticmethod
    def listar_id():
        # para listar o treino com um determinado id;
        pass
    
    @staticmethod
    def atualizar():
        # para atualizar os dados de um treino;
        pass

    @staticmethod
    def excluir():
        # para excluir um treino da lista;
        pass

    @staticmethod
    def maisRapido():
        # para mostrar o treino em que o atleta obteve a maior velocidade média.
        pass