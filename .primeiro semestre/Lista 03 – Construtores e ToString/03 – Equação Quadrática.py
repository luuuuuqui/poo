'''
Escrever uma classe para resolver uma Equação do 2o grau.

A classe deve calcular o delta e as raízes de uma equação do segundo grau, com base nos coeficientes a, b e c de
uma equação f(x) = ax2 + bx + c. O construtor da classe recebe os valores iniciais dos atributos. Os métodos de acesso podem alterar e recuperar esses valores.

O método Delta retorna o valor do delta usado no cálculo das raízes. O método TemRaizesReais retorna um booleano informando se a equação tem ou não raízes reais; o método Raiz1 retorna a primeira raiz e Raiz2, a segunda. 

O método ToString deve retornar um texto com os atributos do objeto.

Desenhe o diagrama UML da classe.
'''

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

    # (-b ± √(b² - 4 * a * c) * 0.5) / (2 * a)

    def calc_delta(self):
        self.__delta = self.__b ** 2 - 4 * self.__a * self.__c
        return self.__delta
    
    def temRaizesReais(self):
        if self.calc_delta() < 0: return False
        return True
    
    def Raiz1(self):
        return (-self.__b + self.calc_delta() * 0.5) / (2 * self.__a)

    def Raiz2(self):
        return (-self.__b - self.calc_delta() * 0.5) / (2 * self.__a)


class UI:
    @staticmethod
    def menu():
        op = int(input("\nInforme uma opção:\n  1: Equação Quadrática,\n  9: Fim.\nOpção selecionada: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.equaçãoQuadrática()
    @staticmethod
    def equaçãoQuadrática():
        eq = EquaçãoQuadrática()
        print("\nEquação: Quadrática (ax² + bx + c)")
        eq.set_a(float(input("  Informe o valor de a: ")))
        eq.set_b(float(input("  Informe o valor de b: ")))
        eq.set_c(float(input("  Informe o valor de c: ")))

        print(f"\nEquação: {eq.get_a()}x² + {eq.get_b()}x + {eq.get_c()}")
        print(f"  Delta: {eq.calc_delta()}")
        print(f"  Tem raízes reais? {'Sim' if eq.temRaizesReais() else 'Não'}.")
        print(f"  Raiz 1: {eq.Raiz1()}")
        print(f"  Raiz 2: {eq.Raiz2()}")

UI.main()




