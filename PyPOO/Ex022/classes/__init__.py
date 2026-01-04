'''Implemente as classes Motor e Carro.

A classe Motor deve ter os atributos tipo (por exemplo, "V8", "Elétrico") e potencia (em cavalos).
A classe Carro deve ter os atributos modelo, ano e um atributo que seja um objeto da classe Motor.
Crie um método no Carro para exibir as informações completas do carro, incluindo as características do motor.

Teste criando diferentes carros com diferentes tipos de motores.'''
class Motor:
    def __init__(self, tipo, movido, potencia):
        self.tipo = tipo
        self.movido = movido
        self.potencia = potencia
class Carro:
    def __init__(self, modelo, ano, motor):
        self.modelo = modelo
        self.ano = ano
        self._motor = None
        self.motor = motor
        self.info_carro = {
            'Modelo': self.modelo,
            'Ano': self.ano,
            'Motor': self.motor.tipo,
            'Movido': self.motor.movido,
            'Potência': f'{self.motor.potencia} cavalos'
        }
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, valor):
        if isinstance(valor, Motor):
            self._motor = valor
        else:
            raise ValueError('sla')

    def exibir_info_carro(self):
        print('-'*30)
        print(f'INFO DO CARRO {self.modelo}')
        print('-'*30)
        for e , (chave, valor) in enumerate(self.info_carro.items()):
            print(f'{e+1}° - {chave}: {valor}')
m1 = Motor('V8', 'Eletricidade', 200)
c1 = Carro('BMW', 2019, m1)
c1.exibir_info_carro()
m2 = Motor('VX', 'Hibrido', 540)
m4 = 'Não sou um motor'
c2 = Carro('Ferrari', 2025, m2)
c2.exibir_info_carro()