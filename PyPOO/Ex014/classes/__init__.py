class Estudante:
    dados_dic = dict()
    def __init__(self, nome, idade, nota):
        self.__nome = nome
        self.__idade = idade
        self.__nota = nota
        Estudante.dados_dic[self.__nome] = {
            'nome': self.__nome,
            'idade': self.__idade,
            'nota': self.__nota
        }

    def modificar(self, nova_chave, chave=''):
        if chave == 'nome':
            Estudante.dados_dic[self.__nome]['nome'] = nova_chave
        elif chave == 'idade' and nova_chave >= 18:
            Estudante.dados_dic[self.__nome]['idade'] = nova_chave
        elif chave == 'nota' and 10 >= nova_chave >= 0:
            Estudante.dados_dic[self.__nome]['nota'] = nova_chave
        else:
            raise ValueError(f'O valor tem que estar dentro das regras')

    def dados(self):
        print(f'{"DADOS DO ESTUDANTE:":^30}')
        cont = 0
        print(f'{Estudante.dados_dic[self.__nome]["nome"]:^30}')
        for chave, valor in Estudante.dados_dic[self.__nome].items():
            if cont > 0:
                print(f'{chave:>15} {valor:<15}')
            cont += 1

p1 = Estudante('Fellipe', 15, 9)
p1.modificar(34, 'idade')
p1.modificar(4, 'nota')
p1.modificar('Pedro', 'nome')
p1.dados()

