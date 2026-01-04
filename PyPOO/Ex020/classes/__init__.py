'''Crie uma classe Motor com o atributo potencia.
Crie outra classe Carro que possui um motor como atributo.
O motor deve ser passado para o carro no momento da sua criação, demonstrando a relação de agregação.

Requisitos:

Crie dois motores com diferentes potências.
Crie dois carros utilizando os motores criados.
Exiba a potência do motor de cada carro.'''
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
class Carro:
    def __init__(self, motor):
        self.motor = motor
    def exibir_potencia(self):
        print(f'A potência do motor é de {self.motor.potencia} cavalos')
motor1 = Motor(5)
motor2 = Motor(2)
carro1 = Carro(motor1)
carro2 = Carro(motor2)
carro2.exibir_potencia()