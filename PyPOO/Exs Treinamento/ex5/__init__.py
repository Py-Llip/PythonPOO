"""### **3. Construtores com super()**
Crie uma classe base `Veiculo` com atributos `marca` e `modelo`.
Crie uma classe derivada `Carro` que adiciona o atributo `num_portas`. Use o método `super()` para inicializar os atributos herdados."""
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def iniciar(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}')
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        self.num_portas = num_portas
        super().__init__(marca, modelo)
    def iniciar(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nNúmeros de portas {self.num_portas}')
helicopter = Veiculo('SemMarca', 'SemModelo')
car = Carro('SemMarca', 'SemModelo', 4)
helicopter.iniciar()
car.iniciar()