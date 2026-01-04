'''from PyPOO.Ex001.teste import Pessoa
#p1 = Pessoa.por_ano_nasci('Fellipe', 2009)
p1 = Pessoa('Fellipe', 15)
print(p1)
print(p1.nome, p1.idade)
p1.ano_nasci()'''
class Personagem:
    def __init__(self, nome, forca, protecao):
        self.nome = nome
        self.__forca = forca
        self.protecao = protecao
    def get_forca(self):
        return self.__forca
    def set_forca(self, nova_forca):
        self.__forca = nova_forca
    def estatisiticas(self):
        print(self.nome, self.__forca, self.protecao)
    def acrescentar(self, forca):
        self.__forca += forca
p1 = Personagem('LexLlip', 50, 250)
p1.set_forca(12)
p1.acrescentar(1000)
p1.estatisiticas()
print(p1.get_forca())
