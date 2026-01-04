"""Exercício 2: Sistema de Pagamento
Implemente um sistema de pagamento utilizando classes abstratas.

Crie uma classe abstrata Pagamento que:
Possui um método abstrato processar_pagamento() que deve ser implementado por todas as subclasses.
Possui um atributo valor para armazenar o valor do pagamento.
Implemente duas classes concretas que herdam de Pagamento:
CartaoCredito, que imprime "Pagamento de [valor] processado com cartão de crédito."
Boleto, que imprime "Pagamento de [valor] processado com boleto."
Teste sua implementação criando objetos de ambas as classes e chamando o método processar_pagamento()."""
from abc import ABC, abstractmethod
class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor
    @abstractmethod
    def processar_pagamento(self):
        pass
class CartaoCredito(Pagamento):
    def processar_pagamento(self):
        print(f'Pagamento de {self.valor} processado com cartão de crédito.')
class Boleto(Pagamento):
    def processar_pagamento(self):
        print(f'Pagamento de {self.valor} processado com boleto.')


cartao = CartaoCredito(100)
cartao.processar_pagamento()
boleto = Boleto(50)
boleto.processar_pagamento()