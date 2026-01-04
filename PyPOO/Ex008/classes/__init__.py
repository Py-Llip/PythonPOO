'''Crie uma classe Produto que tenha um método estático calcular_desconto
que recebe o preço original de um produto e a porcentagem de desconto.
O método deve retornar o preço com o desconto aplicado.
Chame o método estático sem criar uma instância da classe.'''
class Produto:
    @staticmethod
    def calcular_desconto(preco, desconto):
        return preco - (preco * desconto / 100)
print(Produto.calcular_desconto(70, 10))