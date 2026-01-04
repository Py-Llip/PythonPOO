'''Crie uma classe base chamada Funcionario com os seguintes atributos e métodos:

Atributos: nome, salario.
Método: exibir_informacoes() - Exiba o nome e o salário do funcionário.
Em seguida, crie uma classe derivada chamada Gerente:

Adicione um atributo adicional: bonus.
Altere o método exibir_informacoes() para exibir também o valor do bônus.
Crie instâncias de Funcionario e Gerente, e exiba as informações de ambos usando o método apropriado.'''
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def exibir_informacoes(self):
        print(f'O nome do funcionário é {self.nome} e o salário é {self.salario}.')
class Gerente(Funcionario):
    def __init__(self, bonus, nome, salario):
        super().__init__(nome, salario)
        self.bonus = bonus
    def exibir_informacoes(self):
        print(f'O nome do gerente é {self.nome}, o salário é {self.salario} e o bônus é {self.bonus}.')
f1 = Funcionario('Pedro', 19000)
g1 = Gerente(15, 'Fellipe', 20000)
f1.exibir_informacoes()
g1.exibir_informacoes()
