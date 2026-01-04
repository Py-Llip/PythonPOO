'''Crie uma classe Pessoa que tenha um atributo de classe contador,
que conta o número de instâncias criadas.
Cada vez que uma nova pessoa for criada, incremente esse contador.
Implemente um método de classe chamado contar_pessoas() que retorna o número total de pessoas criadas.'''
class Pessoa:
    contador = 0
    def __init__(self, sexo, nome='Desconhecido'):
        self.sexo = sexo
        self.seguir()
        self.nome = nome
        Pessoa.contador += 1
    def seguir(self):
        if self.sexo.strip().upper()[0] not in ['M', 'F']:
            raise Exception (f'Erro! {self.sexo} inexistente')
    @classmethod
    def contar_pessoas(cls):
        return cls.contador
