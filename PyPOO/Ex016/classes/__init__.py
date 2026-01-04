'''Crie uma classe Produto que tenha atributos como nome, preço e categoria.
Crie uma classe Loja que tenha um nome e uma lista de produtos.
Adicione métodos para:

Adicionar produtos à loja.
Buscar produtos por categoria.'''
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.lista_produtos = []
    def add_produtos(self, objeto):
        self.lista_produtos.append(objeto)
        print(f'adicionado a lista {objeto.nome}')
    def acionar_categoria(self, categoria):
        for produto in self.lista_produtos:
            if produto.categoria == categoria:
                print(f'O produto {produto.nome} tem o preço {produto.preco} na categoria {produto.categoria}')
                return
        raise ValueError('Esta categoria não foi indentificada')
p1 = Produto('Arroz', 2.50, 'grãos')
loja1 = Loja('Preço Baixo')
loja1.add_produtos(p1)
loja1.acionar_categoria('grãos')
