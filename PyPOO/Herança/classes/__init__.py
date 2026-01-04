class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    def falar(self):
        print(f'{self.nomeclasse} Falando')
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} Estudando')
c1 = Cliente('Fellipe', 15)
a1 = Aluno('Luiz', 16)
c1.falar()
a1.falar()
a1.estudar()
c1.comprar()
p1 = Pessoa('João', 23)
p1.falar()
print(a1.nome)
