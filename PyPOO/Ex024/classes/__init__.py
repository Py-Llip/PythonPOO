'''Crie uma classe base chamada Animal com os seguintes atributos e métodos:

Atributos: nome, idade.
Método: falar() - Exiba uma mensagem dizendo que o animal faz um som.
Em seguida, crie duas classes derivadas:

Cachorro: sobrescreva o método falar() para exibir "O cachorro late".
Gato: sobrescreva o método falar() para exibir "O gato mia".
Teste as classes criando instâncias de Cachorro e Gato, e chame o método falar() de ambas.'''
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f'{self.nome} faz um som.')
class Cachorro(Animal):
    def falar(self):
        print(f'{self.nome} late.')
class Gato(Animal):
    def falar(self):
        print(f'{self.nome} mia.')
a1 = Animal('Capivara', 15)
a1.falar()