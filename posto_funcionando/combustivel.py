class Combustivel:
    def __init__(self, tipo, preco):
        self.tipo = tipo
        self.preco = preco

class Combustiveis:
    DIESEL_S10 = Combustivel("s10", 6.0)
    DIESEL_S500 = Combustivel("s500", 5.7)
    GASOLINA_COMUM = Combustivel("comum", 6.2)
    GASOLINA_ADITIVADA = Combustivel("aditivada", 6.5)

class CombustivelFactory:
    @staticmethod
    def criar(tipo):
        mapa = {
            "s10": Combustiveis.DIESEL_S10,
            "s500": Combustiveis.DIESEL_S500,
            "comum": Combustiveis.GASOLINA_COMUM,
            "aditivada": Combustiveis.GASOLINA_ADITIVADA
        }
        if tipo in mapa:
            return mapa[tipo]
        raise ValueError("Combustível inválido.")
