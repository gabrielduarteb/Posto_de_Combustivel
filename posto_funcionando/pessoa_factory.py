from cliente import Cliente
from funcionario import Funcionario

class PessoaFactory:
    @staticmethod
    def criar_pessoa(tipo, nome):
        tipo = tipo.lower()
        if tipo == "cliente":
            return Cliente(nome)
        elif tipo == "funcionario":
            return Funcionario(nome)
        else:
            raise ValueError("Tipo de pessoa inválido.")
