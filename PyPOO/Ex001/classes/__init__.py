
class Carro:
    def __init__(self, marca='nenhum', modelo='nenhum', ano=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_detalhes(self):
        dicionario = dict()
        dicionario['Marca'] = [self.marca]
        dicionario['Modelo'] = [self.modelo]
        dicionario['Ano'] = [self.ano]
        cont = 1
        for k, v in dicionario.items():
            print(f'{k}: {v}', end='')
            if cont < len(dicionario):
                print(',', end=' ')
            else:
                print('.')
            cont += 1

