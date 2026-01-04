'''Crie uma classe Carro que tenha um atributo de classe carros_registrados
(uma lista). Cada vez que um novo carro for criado, adicione o carro à lista.
Implemente um método de classe chamado mostrar_carros() que exibe todos os carros registrados.'''
class Carro:
    carros_registrados = list()
    def __init__(self, modelo):
        self.modelo = modelo
        Carro.carros_registrados.append(self)
    @classmethod
    def mostrar_carros(cls):
        for carro in cls.carros_registrados:
            print(carro.modelo)
