class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 5000)
p3 = Produto('Caneta', 15)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.lista_produtos()
print(carrinho.soma_total())


