from rich import print, inspect

class Funcionario:
    # Atributos de classe
    empresa = 'Curso em Vídeo'
    def __init__(self, nome: str='Desconhecido', setor: str='Desconhecido', cargo: str='Desconhecido'):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print(':pen:Funcionário cadastrado!')

    def apresentar(self) -> str:
        return f':point_right:Olá, sou [blue]{self.nome}[/], estou no setor de [blue]{self.setor}[/blue] e trabalho no cargo de [blue]{self.cargo}[/] da empresa {Funcionario.empresa}' #self.__class__.empresa

if __name__ == '__main__':


    f1 = Funcionario()
    f2 = Funcionario('Fellipe', 'Tecnologia', 'Criação de IA')
    Funcionario.empresa = "Hostnet"
    f1.empresa = 'EstudoNauta'
    print(f1.empresa)
    print(f1.apresentar())
    print(f2.apresentar())
    #inspect(f1)
    #inspect(f2)
    #inspect(Funcionario)