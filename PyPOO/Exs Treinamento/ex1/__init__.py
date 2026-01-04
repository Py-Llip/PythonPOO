'''
1. Criando uma Hierarquia com Métodos Específicos
Exercício:
Crie uma classe base chamada FormaGeometrica com um método calcular_area()
que imprime "Área não definida". Crie duas classes derivadas, Quadrado e Circulo, que implementam o cálculo de área para suas respectivas formas.

Explicação:
Ensina como sobrescrever métodos na herança para comportamentos específicos.'''
class FormaGeometrica:
    def calcular_area(self):
        print(f'Área não definida.')
class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado ** 2
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        return self.raio ** 2 * 3.14