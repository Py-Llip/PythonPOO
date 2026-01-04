"""### **4. Sobreposição parcial**
Crie uma classe `Pessoa` com atributos `nome` e `idade`, e um método `cumprimentar()` que diz "Olá, meu nome é [nome]".
Crie uma classe derivada `Professor` que sobrescreve `cumprimentar()` para adicionar "Eu sou professor"."""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        print(f'Olá, meu nome é {self.nome}')
class Professor(Pessoa):
    def cumprimentar(self):
        print(f'Olá, sou o professor {self.nome}')
guarda = Pessoa('Fellipe', 19)
professor = Professor('Jirafares', 43)
guarda.cumprimentar()
professor.cumprimentar()