class Venda:
    def __init__(self, pessoa, frentista, pagamento, valor):
        self.pessoa = pessoa
        self.frentista = frentista
        self.pagamento = pagamento
        self.valor = valor
    def finalizar(self):
        return self.pagamento.pagar(self.valor)
