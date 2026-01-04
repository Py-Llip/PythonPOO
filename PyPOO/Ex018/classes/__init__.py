'''Crie uma classe chamada Aluno com os atributos nome e idade.
Crie outra classe chamada Turma que possui um atributo alunos, que será uma lista de objetos do tipo Aluno.
Implemente métodos para adicionar e listar os alunos da turma.

Requisitos:

Crie 3 alunos e adicione-os a uma turma.
Liste todos os alunos dessa turma.'''
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Turma:
    def __init__(self):
        self.alunos = []
    def adicionar(self, objeto):
        if objeto in self.alunos:
            print(f'Já existe o aluno {objeto.nome} na turma')
        else:
            self.alunos.append(objeto)
    def listar(self):
        if not self.alunos:
            print('Não existe alunos ainda')
        else:
            for e, objeto in enumerate(self.alunos):
                print(f'N°{e+1} - Nome: {objeto.nome} - idade: {objeto. idade}')

a1 = Aluno('Fellipe', 15)
a2 = Aluno('Pedro', 17)
a3 = Aluno('Eduarda', 14)
e = Turma()
e.adicionar(a1)
e.adicionar(a2)
e.adicionar(a3)
e.listar()
