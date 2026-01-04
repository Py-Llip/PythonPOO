"""Crie duas classes: Motor e Carro. A classe Carro deve ter um atributo que seja uma instância da classe Motor.
 A classe Motor deve ter um método chamado ligar, e o método da classe Carro deve chamar o método ligar do motor."""
class Engine:
    def on(self):
        print(f'Ligando motor.')
        print(f'Motor ligado com sucesso!')
class Carro:
    def __init__(self, name):
        self.engine = Engine()
    def on(self):
        self.engine.on()
carro = Carro('Fiat')
carro.on()