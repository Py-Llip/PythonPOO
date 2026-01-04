class ContaBancaria:
    def __init__(self, nome_titular='Desconhecido', saldo=0):
        self.nome_titular = nome_titular
        self.saldo = saldo
    def depositar(self, valor=0):
        self.saldo += valor
    def sacar(self, valor=0):
        self.saldo -= valor
    def exibir_saldo(self):
        print(f'Saldo atual: R$ [{self.saldo:.2f}]')

