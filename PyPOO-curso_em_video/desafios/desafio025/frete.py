from abc import ABC, abstractmethod

class Transporte(ABC):
    fator = 0
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = self.__class__.fator

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.5

    def calc_frete(self):
        return f'R${self.frete*self.distancia:.2f}'


class Caminhao(Transporte):
    fator = 1.2

    def calc_frete(self) -> str:
        if self.distancia >= 50:
            return f'R${self.frete * self.distancia:.2f}'
        return f'Raio mínimo de 50Km'


class Drone(Transporte):
    fator = 9.5

    def calc_frete(self):
        if self.distancia <= 10:
            return f'R${self.frete * self.distancia:.2f}'
        return f'O raio máximo de 10Km'

