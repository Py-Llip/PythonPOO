class ContaBancaria:
    dic_contas = dict()
    def __init__(self, num_conta, saldo=0):
        self.__num_conta = num_conta
        self.__saldo = saldo
        ContaBancaria.dic_contas[num_conta] = self

    def acessar_saldo(self):
        print(f'{self.__num_conta}, saldo de: R${self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print(f'Não é possível sacar R${valor}')

    @classmethod
    def consultar_conta(cls, num_conta):
        conta = cls.dic_contas.get(num_conta)
        if conta:
            conta.acessar_saldo()
        else:
            print('Conta inexistente')


p1 = ContaBancaria(1, 100)
p2 = ContaBancaria(2, 190)
p1.acessar_saldo()
p1.depositar(50)
p1.acessar_saldo()
p1.sacar(151)
p1.acessar_saldo()
ContaBancaria.consultar_conta(3)