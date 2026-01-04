'''Implemente uma classe Aluno com os atributos nome e série.
Crie uma classe Escola com os atributos nome e uma lista de alunos.
Adicione métodos para:

Matricular alunos.
Mostrar a lista de alunos matriculados.
Encontrar um aluno pelo nome.'''
class Aluno:
    def __init__(self, nome, serie):
        self.nome = nome
        self.serie = serie
class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.lst_alunos = []
    def matricular(self, aluno):
        for c in self.lst_alunos:
            if c.nome == aluno.nome:
                raise ValueError(f'O aluno {aluno.nome} já está cadastrado')
        self.lst_alunos.append(aluno)
    def mostrar_matriculas(self):
        for c in self.lst_alunos:
            print(c.nome)
    def mostrar_aluno(self, nome):
        for e, c in enumerate(self.lst_alunos):
            if c.nome == nome:
                print(f'Aluno(a) {e+1}°, nome {c.nome} na série {c.serie}')
a1 = Aluno('Fellipe', 9)
a2 = Aluno('Pedro', 10)
e1 = Escola('Aloisio')
e1.matricular(a1)
e1.matricular(a2)
e1.mostrar_matriculas()
e1.mostrar_aluno('Fellipe')
