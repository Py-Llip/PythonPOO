import abc #Abstract Base Classes
import math
class Figura(abc.ABC):

    def __init__(self, cor):
        self.__cor = cor

    @abc.abstractmethod
    def calculararea(self):
        pass
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.cor = cor
class Circulo(Figura):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio
    @property
    def raio(self):
        return self.__raio
    @raio.setter
    def raio(self, raio):
        self.__raio = raio
    def calculararea(self):
        return math.pi * self.__raio ** 2
class Quadrado(Figura):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.__lado = lado
    @property
    def lado(self):
        return self.__lado
    @lado.setter
    def lado(self, lado):
        self.__lado = lado
    def calculararea(self):
        return self.__lado ** 2
c1 = Circulo('Vermelho', 5)
q1 = Quadrado('Verde', 10)
c2 = Circulo('Azul', 7)
print(c1.calculararea())