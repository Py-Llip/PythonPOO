from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, vlr_lado: float | int = 4):
        self.vlr_lado = vlr_lado

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def perimetro(self):
        return self.vlr_lado * 4

    def area(self):
        return self.vlr_lado**2

class Circulo(Poligono):
    def perimetro(self):
        return 2*3.1415*self.vlr_lado

    def area(self):
        return 3.1415*self.vlr_lado**2
