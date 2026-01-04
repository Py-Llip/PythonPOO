'''Crie uma classe base chamada Veiculo com:

Atributos: marca, modelo, ano.
Método: detalhes() - Exiba as informações do veículo.
Crie duas classes derivadas:

Carro: Adicione o atributo portas (número de portas) e modifique o método detalhes() para exibir esse atributo.
Moto: Adicione o atributo cilindradas (capacidade do motor) e modifique o método detalhes() para exibir esse atributo.
Crie um objeto de cada classe e chame o método detalhes() para verificar se os detalhes são exibidos corretamente.Crie uma classe base chamada Veiculo com:

Atributos: marca, modelo, ano.
Método: detalhes() - Exiba as informações do veículo.
Crie duas classes derivadas:

Carro: Adicione o atributo portas (número de portas) e modifique o método detalhes() para exibir esse atributo.
Moto: Adicione o atributo cilindradas (capacidade do motor) e modifique o método detalhes() para exibir esse atributo.
Crie um objeto de cada classe e chame o método detalhes() para verificar se os detalhes são exibidos corretamente.'''
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def detalhes(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}')
class Carro(Veiculo):
    def __init__(self, portas, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.portas = portas
    def detalhes(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nNúmero de portas: {self.portas}')
class Moto(Veiculo):
    def __init__(self, cilindradas, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    def detalhes(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCapacidade do motor: {self.cilindradas}.')

v1 = Veiculo('Fiat', 2009, 2008)
c1 = Carro(4, 'BMW', 'Ex3z', 2023)
m1 = Moto('4V', 'Suziki', 'Er43', 1980)
v1.detalhes()
c1.detalhes()
m1.detalhes()