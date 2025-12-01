class Pagamento:
    def pagar(self, valor):
        return valor

class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        return valor * 1.02

class PagamentoPix(Pagamento):
    def pagar(self, valor):
        return valor * 0.98

class PagamentoDinheiro(Pagamento):
    pass
