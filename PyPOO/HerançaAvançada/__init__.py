# Herança Multipla:
class Pail:
    def metodo_pai1(self):
        print('Método do Pai 1')
class Pail2:
    def metodo_pai2(self):
        print('Método do Pai 2')
class Filho(Pail, Pail2):
    def metodo_filho(self):
        print('Método do Filho')
filho = Filho()
filho.metodo_filho()
filho.metodo_pai1()
filho.metodo_pai2()
print(Filho.__mro__)