'''Crie uma classe Produto que tenha um atributo de classe estoque (uma lista).
 Cada vez que um novo produto for criado, adicione o produto à lista.
  Implemente um método de classe chamado calcular_preco_total() que calcula e retorna o preço total de todos os produtos no estoque.'''
from PyPOO.Ex004.classes import Produto
p1 = Produto('Feijão', 2.99)
p2 = Produto('Arroz', 5.99)
p3 = Produto('Milharina', 10.50)
print(p1.calcular_preco_total())