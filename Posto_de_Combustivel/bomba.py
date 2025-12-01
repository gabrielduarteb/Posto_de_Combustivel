class Bomba:
    def __init__(self, combustivel, estoque, frentista):
        self.combustivel = combustivel
        self.estoque = estoque
        self.frentista = frentista

    def abastecer(self, litros_solicitados):
        estoque_atual = self.estoque.get_estoque(self.combustivel.tipo)
        if litros_solicitados <= estoque_atual:
            self.estoque.reduzir(self.combustivel.tipo, litros_solicitados)
            return litros_solicitados, litros_solicitados * self.combustivel.preco
        litros_possiveis = estoque_atual
        self.estoque.reduzir(self.combustivel.tipo, litros_possiveis)
        return litros_possiveis, litros_possiveis * self.combustivel.preco
