class Pessoa:
    ano = 2024
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def ano_nasci(self):
        print(self.ano - self.idade)

    @classmethod
    def por_ano_nasci(cls, nome, ano_nasci):
        idade = cls.ano - ano_nasci
        return cls(nome, idade)
