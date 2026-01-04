'''Crie uma classe Pessoa com um atributo estático contagem que mantém o número de instâncias da classe criadas.
Implemente um método estático obter_contagem que retorna o valor do atributo contagem.
Teste a classe criando algumas instâncias e chamando o método estático.'''
class Pessoa:
    contagem = 0
    def __init__(self):
        Pessoa.contagem += 1
    @staticmethod
    def obter_contagem():
        return Pessoa.contagem
p1 = Pessoa()
p2 = Pessoa()
print(Pessoa.obter_contagem())