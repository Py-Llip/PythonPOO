class ContaBancaria:

    """
Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id # publico (+)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')

    def __str__(self):
        #return f'A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo.'
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        valor = abs(valor)
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
            return
        print(f'Saque negado de R${valor:,.2f} na conta {self.id}: __saldo insuficiente')


#c1 = ContaBancaria(112, 'Fellipe', 3000)
#c1.depositar(500)
#c1.sacar(2_000_000)
#print(c1)
