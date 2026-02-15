from rich import print

class Caneta:
    def __init__(self, cor:str='azul'):
        self.cores = {'azul': 'blue',
                      'vermelha': 'red',
                      'verde': 'green',
                      'amarela': 'yellow',
                      'preta': 'black',
                      'branca': 'white'
                      }
        if cor not in self.cores.keys():
            raise NameError(f'A caneta de cor {cor} não existe!')
        self.cor = cor
        self._destampado = False

    def destampar(self):
        self._destampado = True

    def tampar(self):
        self._destampado = False

    def escrever(self, texto:str):
        if not self._destampado:
            print(f'Caneta de cor [{self.cores[self.cor]}]{self.cor}[/] tampada!')
            return
        print(f'[{self.cores[self.cor]}]{texto}[/]', end='')

    def quebrar_linha(self, linhas:int=1):
        if linhas > 0:
            print('\n' * (linhas-1))

c1 = Caneta('preta')
c1.destampar()
c1.escrever('Olá, Mundo! ')
c1.tampar()
c1.escrever('Outro texto')
c1.quebrar_linha(2)
c2 = Caneta('amarela')
c2.destampar()
c2.escrever('Essa é a cor amarela')

