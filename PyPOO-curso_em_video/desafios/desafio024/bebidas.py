from abc import ABC,abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print(f'{"-"*3} Iniciando o Preparo {"-"*3}')
        print(f'1 {self.ferver_agua()}')
        e = 2
        for i in vars(self.__class__).items():
            if callable(i[1]) and not i[0].startswith('__'):
                print(f'{e} {i[1](self)}')
                e += 1
        print(f'{"-" * 3} Bebida Pronta {"-" * 3}')

    def ferver_agua(self):
        return 'Fervendo água a 100 graus Celsius'
    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        return 'Passando água pressurizada pelo pó de café moído'
    def servir(self):
        return 'Servindo em xícara pequena.'

class Cha(BebidaQuente):
    def misturar(self):
        return 'Mergulhando o sachê de ervas na água'
    def servir(self):
        return 'Servindo na canela de porcelana com limão'

class Leite(BebidaQuente):
    def misturar(self):
        return 'Passando vapor pressurizante pelo bico do leite'
    def servir(self):
        return 'Servindo na caneca grande, já com café'

if __name__ == '__main__':
    b = Leite()
    b.preparar()