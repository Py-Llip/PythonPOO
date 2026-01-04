'''Crie uma classe Produto que tenha um atributo de classe estoque (uma lista).
 Cada vez que um novo produto for criado, adicione o produto à lista.
  Implemente um método de classe chamado calcular_preco_total() que calcula e retorna o preço total de todos os produtos no estoque.'''
class Produto:
    estoque = list()
    def __init__(self, produto='Desconhecido', preco=0.0):
        self.produto = produto
        self.preco = preco
        Produto.estoque.append(self)
    @classmethod
    def calcular_preco_total(cls):
        soma = 0
        for produto in cls.estoque:
            soma += produto.preco
        return soma


