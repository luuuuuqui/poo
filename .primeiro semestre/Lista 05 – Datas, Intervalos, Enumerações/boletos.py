'''
2. Um Boleto
Escreva a classe Boleto e a enumeração Pagamento de acordo com o diagrama UML apresentado abaixo.
• A classe deve ter como atributos os dados de um boleto com informações sobre código de barras, datas, valores
e situação de pagamento;
• O construtor da classe recebe os dados iniciais de um boleto;
• O método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto;
• O método Situacao retorna a situação de pagamento do boleto que pode ser: Em Aberto, quando o pagamento
ainda não foi realizado; Pago Parcial, quando o valor pago for menor que o valor do boleto; ou Pago, quando o
valor do pagamento corresponder ao valor do boleto;
• O método ToString deve retornar um texto com os atributos do objeto;
• A enumeração Pagamento é usada para listar os possíveis valores das situações de pagamento de um boleto.
• Inclua métodos de acesso na classe para permitir alterar e recuperar os dados de um boleto (não apresentados
no diagrama;
• Faça uma UI para testar a classe e a enumeração.
'''

import datetime

class Boleto:
    def __init__(self):
        self.set_codBarras('12345678901234567890123456789012345678901234567890')
        self.set_dataEmissao(datetime.date.today())
        self.set_dataVencimento(datetime.date.today() + datetime.timedelta(days=30))
        self.set_dataPagto(None)
        self.set_valorBoleto(100.0)
        self.set_valorPago(None) # dinheiro não seria int, ao invés de decimal? já que int não teria problemas com erros de arredondamento...
        self.set_situacao('EM ABERTO')
    
    def set_codBarras(self, codBarras):
        if isinstance(codBarras, str) and codBarras.strip() and len(codBarras) == 44:
            self.__codBarras = codBarras.strip()
        else:
            raise ValueError("Código de barras inválido. Deve ser uma string não vazia.")
        
    def get_codBarras(self):
        return self.__codBarras
    
    def set_dataEmissao(self, dataEmissao):
        if isinstance(dataEmissao, datetime.date):
            self.__dataEmissao = dataEmissao
        else:
            raise ValueError("Data de emissão inválida. Deve ser um objeto datetime.date.")
    
    def get_dataEmissao(self):
        return self.__dataEmissao
    
    def set_dataVencimento(self, dataVencimento):
        if isinstance(dataVencimento, datetime.date):
            self.__dataVencimento = dataVencimento
        else:
            raise ValueError("Data de vencimento inválida. Deve ser um objeto datetime.date.")
        
    def get_dataVencimento(self):
        return self.__dataVencimento
    
    def set_dataPagto(self, dataPagto):
        if isinstance(dataPagto, datetime.date):
            self.__dataPagto = dataPagto
        else:
            raise ValueError("Data de pagamento inválida. Deve ser um objeto datetime.date.")
        
    def get_dataPagto(self):
        return self.__dataPagto
    
    def set_valorBoleto(self, valorBoleto):
        if isinstance(valorBoleto, (int, float)) and valorBoleto >= 0:
            self.__valorBoleto = float(valorBoleto)
        else:
            raise ValueError("Valor do boleto inválido. Deve ser um número não negativo.")
        
    def get_valorBoleto(self):
        return self.__valorBoleto
    
    def set_valorPago(self, valorPago):
        if isinstance(valorPago, (int, float)) and valorPago >= 0:
            self.__valorPago = float(valorPago)
        else:
            raise ValueError("Valor pago inválido. Deve ser um número não negativo.")
        
    def get_valorPago(self):
        return self.__valorPago
    
    def get_situacao(self):
        if self.__valorPago == 0:
            return 'EM ABERTO'
        elif self.__valorPago < self.__valorBoleto:
            return 'PAGO PARCIALMENTE'
        else:
            return 'PAGO'
    
    def set_situacao(self, situacao):
        if situacao in ['EM ABERTO', 'PAGO PARCIALMENTE', 'PAGO']:
            self.__situacao = situacao
        else:
            raise ValueError("Situação inválida. Deve ser 'EM ABERTO', 'PAGO PARCIALMENTE' ou 'PAGO'.")
    
    def pagar(self, valorPago):
        if valorPago < 0:
            raise ValueError("Valor pago não pode ser negativo.")
        self.__valorPago += valorPago
        if self.__valorPago >= self.__valorBoleto:
            self.set_situacao('PAGO')
            self.__dataPagto = datetime.date.today()
        else:
            self.set_situacao('PAGO PARCIALMENTE')
    
