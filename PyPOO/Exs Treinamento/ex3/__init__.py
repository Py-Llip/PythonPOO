'''Crie uma classe base `Animal` com o método `comer()` que imprime "O animal está comendo".
 Crie uma classe derivada `Cachorro` que sobrescreve `comer()` mas ainda chama o método original usando `super()`.

**Explicação:**
Mostra como usar `super()` para reutilizar métodos na classe base.'''
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print(f'O {self.nome} está comendo')
class Cachorro(Animal):
    def comer(self):
        super().comer()
        print(f'O {self.nome} está comendo ração')
a1 = Animal('Leao')
a2 = Cachorro('Cachorro')
a1.comer()
a2.comer()