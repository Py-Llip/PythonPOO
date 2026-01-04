'''Crie uma classe Calculadora que tenha um método estático
soma que recebe dois números como parâmetros e retorna a soma desses números.
Em seguida, crie um objeto da classe e chame o método soma diretamente pela classe,
sem instanciar um objeto da classe.'''
class Calculadora:
    @staticmethod
    def soma(num1=0, num2=0):
        return num1 + num2

objeto = Calculadora.soma(5, 7)
print(objeto)