class Aluno:
    def __init__(self, nota):
        self.nota = nota
    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, new_nota):
        if 0 <= new_nota <= 10:
            self._nota = new_nota
        else:
            if new_nota > 10:
                raise ValueError('A nota está acima do que permitido.')
            if new_nota < 0:
                raise ValueError('A nota está abaixo do que permitido.')
aluno1 = Aluno(100)
print(aluno1.nota)
