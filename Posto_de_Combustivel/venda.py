class Venda:
    def __init__(self, cliente, funcionario, pagamento, valor):
        self.cliente = cliente
        self.funcionario = funcionario 
        self.pagamento = pagamento
        self.valor = valor

    def finalizar(self):
        valor_final = self.pagamento.pagar(self.valor)
        print(f"Venda realizada por: {self.funcionario.nome}")  
        return valor_final
