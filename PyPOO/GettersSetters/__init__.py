from datetime import date
class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        if not isinstance(value, date):
            raise ValueError('data_nascimento deve ser do tipo date')
        self._data_nascimento = value

    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days


p1 = Pessoa('Fellipe', date(2009, 8, 25))
print(p1.dias_vividos())

