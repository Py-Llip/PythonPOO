"""Exercício 3: Polimorfismo com Listas de Objetos
Descrição: Crie uma classe base chamada Animal com o método fazer_som().
 Em seguida, crie duas classes derivadas chamadas Cachorro e Gato, que sobrescrevem o método fazer_som() para imprimir o som característico de cada um.
  Por fim, crie uma lista de objetos Animal, com instâncias de Cachorro e Gato, e use um laço para chamar o método fazer_som() de cada animal.

Passos:

Crie a classe base Animal com o método fazer_som().
Crie a classe Cachorro que sobrescreve fazer_som() e imprime "Au Au".
Crie a classe Gato que sobrescreve fazer_som() e imprime "Miau".
Crie uma lista de objetos Animal e adicione instâncias de Cachorro e Gato.
Use um laço for para chamar o método fazer_som() de cada objeto na lista."""
class Animal:
    def make_sound(self):
        print('Make sound!')
class Canine(Animal):
    def make_sound(self):
        print('Woo wow!')
class Feline(Animal):
    def make_sound(self):
        print('Meow meow!')
animal = [Canine(), Feline()]
for i in animal:
    i.make_sound()

