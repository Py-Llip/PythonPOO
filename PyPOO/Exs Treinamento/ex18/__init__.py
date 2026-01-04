"""Crie uma classe abstrata chamada Veiculo com os seguintes métodos abstratos:

ligar()
desligar()
mover()
Implemente duas subclasses:

Carro: Pode ligar, desligar e se mover.
Bicicleta: Não precisa "ligar", mas pode "mover".
Adicione métodos e atributos adicionais para personalizar cada classe, como combustivel para o carro e numero_de_marchas para a bicicleta.

Teste o comportamento de cada classe com instâncias concretas."""
import abc
class Veiculo(abc.ABC):
    @abc.abstractmethod
    def ligar(self):
        pass

    @abc.abstractmethod
    def desligar(self):
        pass

    @abc.abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        self.litros = None
    def ligar(self):
        print('Ligado')
    def desligar(self):
        print('Desligado')
    def mover(self):
        print('Movendo')
    def combustivel(self, litros):
        self.litros = litros
        print('adicionado!', self.litros)
class Bicicleta(Veiculo):
    def mover(self):
        print('Movendo')
    def num_marchas(self, marchas):
        print('Trocado!', marchas)
    def ligar(self):
        raise Exception('Bicicleta não tem capacidade de ligar.')
    def desligar(self):
        raise Exception('Bicicleta não tem capacidade de desligar')
d = Bicicleta()
d.num_marchas(14)