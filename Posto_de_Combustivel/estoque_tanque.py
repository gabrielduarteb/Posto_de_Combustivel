class EstoqueTanque:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.estoques = {
                "comum": 10000,
                "aditivada": 5000,
                "s10": 30000,
                "s500": 30000
            }
        return cls._instancia

    def get_estoque(self, tipo):
        return self.estoques.get(tipo, 0)

    def reduzir(self, tipo, litros):
        estoque_atual = self.get_estoque(tipo)
        if litros <= estoque_atual:
            self.estoques[tipo] -= litros
        else:
            self.estoques[tipo] = 0
