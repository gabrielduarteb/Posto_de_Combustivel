Explicação do projeto — Sistema de Posto de Combustível

Visão geral

Este projeto é uma simulação simples de um posto de combustível escrita em Python, organizada em arquivos separados para cada responsabilidade. Ele demonstra os pilares da Programação Orientada a Objetos (abstração, encapsulamento, herança e polimorfismo) e aplica os padrões de projeto Factory e Strategy. Também há uso do Singleton para gerenciar o estoque.



Como o projeto demonstra os pilares da POO

Abstração: cada classe modela um conceito claro (Pessoa, Combustível, Bomba, Estoque, Venda). Usuário do objeto não precisa saber detalhes internos.


Encapsulamento: atributos como estoques e métodos como reduzir() escondem a lógica interna; outras classes chamam apenas métodos públicos.


Herança: Cliente e Funcionario herdam de Pessoa.


Polimorfismo: as classes de pagamento (PagamentoPix, PagamentoCartao, PagamentoDinheiro) implementam a mesma interface pagar() e podem ser trocadas sem alterar Venda.



Padrões de projeto aplicados

Factory Pattern
PessoaFactory e CombustivelFactory: centralizam criação de objetos e isolam a lógica de inicialização.

Strategy Pattern
pagamento_strategy.py: troca dinâmica do algoritmo de cálculo do valor a pagar.

Singleton
EstoqueTanque: garante uma única fonte de verdade para o estoque do posto.
