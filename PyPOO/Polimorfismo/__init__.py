#Polimorfismo
class Veiculo:
    def mover(self):
        print("Movendo")
class Carro(Veiculo):
    def mover(self):
        print("Carro andando")

class Aviao(Veiculo):
    def mover(self):
        print("Avião voando")

# Processar sem classe base exige conhecimento específico das classes:
veiculos = [Carro(), Aviao()]
for veiculo in veiculos:
    veiculo.mover()
