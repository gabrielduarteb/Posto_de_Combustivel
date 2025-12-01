from pessoa_factory import PessoaFactory
from combustivel import Combustivel
from bomba import Bomba
from estoque_tanque import EstoqueTanque
from pagamento_strategy import PagamentoPix, PagamentoCartao, PagamentoDinheiro
from venda import Venda



estoque = EstoqueTanque()




PRECOS = {
    "comum": 6.39,
    "aditivada": 6.49,
    "s10": 5.69,
    "s500": 5.59
}



cliente = PessoaFactory.criar_pessoa("cliente", "Gabriel")
frentista = PessoaFactory.criar_pessoa("funcionario", "João")



bombas = {
    tipo: Bomba(Combustivel(tipo, preco), estoque, frentista)
    for tipo, preco in PRECOS.items()
}





def mostrar_resultado(tipo, litros_solicitados, cliente, pagamento):
    bomba = bombas[tipo]
    combustivel = bomba.combustivel
    litros_reais, valor_bruto = bomba.abastecer(litros_solicitados)
    venda = Venda(cliente, frentista, pagamento, valor_bruto)
    valor_final = venda.finalizar()
    print("\n------------------------------")
    print(f"Frentista: {bomba.frentista.nome}")
    print(f"Cliente: {cliente.nome}")
    print(f"Combustível: {combustivel.tipo.upper()}")
    print(f"Preço por litro: R$ {combustivel.preco:.2f}")
    print(f"Litros solicitados: {litros_solicitados} L")
    print(f"Litros abastecidos: {litros_reais} L")
    if litros_reais < litros_solicitados:
        print("⚠️  Estoque insuficiente! Abastecido somente o que havia disponível.")
    print(f"Valor bruto: R$ {valor_bruto:.2f}")
    print(f"Valor total com pagamento: R$ {valor_final:.2f}")
    print(f"Estoque restante: {estoque.get_estoque(combustivel.tipo)} L")
    print("------------------------------")





if __name__ == "__main__":
    print("\n==== INICIANDO TESTES DO POSTO ====")
    mostrar_resultado("comum", 10, cliente, PagamentoDinheiro())
    mostrar_resultado("s10", 20, cliente, PagamentoCartao())
    mostrar_resultado("aditivada", 30, cliente, PagamentoPix())
    mostrar_resultado("comum", 10000, cliente, PagamentoPix())
    print("==== TESTES FINALIZADOS ====")
