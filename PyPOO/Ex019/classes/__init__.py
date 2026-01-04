'''Implemente os seguintes métodos na classe Empresa:
calcular_folha_pagamento(): Calcula e retorna a soma dos salários de todos os funcionários.
Requisitos:

Crie ao menos 3 funcionários.
Adicione os funcionários à empresa.
Liste todos os funcionários e exiba o valor total da folha de pagamento da empresa.'''
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
class Empresa:
    def __init__(self):
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario):
        if funcionario in self.funcionarios:
            print(f'O funcionário {funcionario.nome} já existe. Não é permitido duplicatas.')
        else:
            self.funcionarios.append(funcionario)
            print('Funcionário cadastrado com sucesso!')
    def listar_funcionarios(self):
        if not self.funcionarios:
            print('Não há funcionários cadastrados.')
        else:
            for e, objeto in enumerate(self.funcionarios):
                print(f'N° {e+1} - Nome: {objeto.nome} - Cargo: {objeto.cargo} - Salário: {objeto.salario}')
    def calcular_folha_pagamento(self):
        soma_salarial = 0
        for objeto in self.funcionarios:
            soma_salarial += objeto.salario
        return soma_salarial
f1 = Funcionario('Fellipe', 'CEO', 504976.8)
f2 = Funcionario('Lucas', 'Diretor de Operações', 34640)
f3 = Funcionario('Rebeca', 'Assistente', 4000)
Lus = Empresa()
Lus.adicionar_funcionario(f1)
Lus.adicionar_funcionario(f2)
Lus.adicionar_funcionario(f3)
Lus.listar_funcionarios()
print(Lus.calcular_folha_pagamento())

