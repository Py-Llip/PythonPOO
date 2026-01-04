"""Exercício 1: Criando uma Classe Abstrata Básica
Implemente uma classe abstrata chamada FormaGeometrica com dois métodos abstratos:

calcular_area()
calcular_perimetro()
Depois, crie duas classes concretas, Retangulo e Circulo, que herdam de FormaGeometrica. Cada classe deve implementar os métodos abstratos com cálculos apropriados.

Dica: Use o módulo abc para criar classes abstratas.
import abc
from math import pi
class FormaGeometrica(abc.ABC):
    @abc.abstractmethod
    def calcular_area(self, *args):
        pass
    @abc.abstractmethod
    def calcular_perimetro(self, *args):
        pass
class Retangulo(FormaGeometrica):
    def calcular_area(self, altura, base):
        return altura * base
    def calcular_perimetro(self, altura, base):
        return 2 * altura + 2 * base
class Circulo(FormaGeometrica):
    def calcular_area(self, raio):
        return pi * raio ** 2
    def calcular_perimetro(self, raio):
        return 2 * pi * raio"""
import abc
from math import pi
class FormaGeometrica(abc.ABC):
    @abc.abstractmethod
    def calcular_area(self):
        pass
    @abc.abstractmethod
    def calcular_perimetro(self):
        pass
class Retangulo(FormaGeometrica):
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return self.altura * self.base
    def calcular_perimetro(self):
        return 2 * self.altura + 2 * self.base
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        return pi * self.raio ** 2
    def calcular_perimetro(self):
        return 2 * pi * self.raio