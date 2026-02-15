from rich import print

class Funcionario:
    def __init__(self, nome: str='Desconhecido', setor: str='Desconhecido', cargo: str='Desconhecido'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print(':pen:Funcionário cadastrado!')

    def apresentar(self):
        print(f':point_right:Olá, sou [blue]{self.nome}[/], estou no setor de [blue]{self.setor}[/blue] e trabalho no cargo de [blue]{self.cargo}[/].')

if __name__ == '__main__':
    f1 = Funcionario()
    f2 = Funcionario('Fellipe', 'Tecnologia', 'Criação de IA')
    f1.apresentar()
    f2.apresentar()