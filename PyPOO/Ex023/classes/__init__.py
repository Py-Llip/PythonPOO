'''Crie as classes Componente e Computador.

A classe Componente deve ter os atributos nome (ex.: "Processador", "Memória RAM") e especificacao (ex.: "Intel i7", "16GB").
A classe Computador deve conter uma lista de componentes e métodos para:
Adicionar componentes.
Exibir a lista completa de componentes do computador.
Teste o programa criando um computador com diferentes componentes.'''
class Componente:
    def __init__(self, nome, especificacao):
        self.nome = nome
        self.especificacao = especificacao
class Computador:
    def __init__(self):
        self.lst_componentes = []
    def add_componentes(self, componente):
        for objeto in self.lst_componentes:
            if componente.especificacao == objeto.especificacao:
                print(f'O {componente.especificacao} já existe')
                return
        self.lst_componentes.append(componente)
    def listar_componentes(self):
        for objeto in self.lst_componentes:
            print(f'- {objeto.nome}: {objeto.especificacao}')
c1 = Computador()
memoria = Componente('Memoria', '32GB')
placa = Componente('PlacaMãe', 'Az3')
c1.add_componentes(memoria)
c1.add_componentes(placa)
c1.listar_componentes()
