"""### **10. Usando isinstance()**
Crie uma hierarquia com classes `Animal`, `Peixe` e `Passaro`.
- Adicione métodos exclusivos a `Peixe` e `Passaro`.
- Crie uma função que recebe uma instância de `Animal` e verifica se é um `Peixe` ou `Passaro` usando `isinstance()`."""
class Animal:
    def __init__(self, nome):
        self.nome = nome
    @staticmethod
    def descobrir(instancia):
        if isinstance(instancia, Peixe):
            print(f'É peixe')
        elif isinstance(instancia, Passaro):
            print('É pássaro')
class Peixe(Animal):
    def nadando(self):
        print(f'Peixe {self.nome} está nadando!')
class Passaro(Animal):
    def voando(self):
        print(f'Pássaro {self.nome} está voando!')
p1 = Peixe('peixebolha')
p2 = Passaro('Passarofolha')
Animal.descobrir(p1)