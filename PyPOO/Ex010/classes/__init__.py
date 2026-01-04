class ContaBancaria:
    def __init__(self, saldo=0):
        self._saldo = saldo
    @property
    def saldo(self):
        print('Verificando o saldo...')
        return self._saldo
    @saldo.setter
    def saldo(self, plus_saldo):
        if not isinstance(plus_saldo, (float, int)):
            raise ValueError('tipo de saldo não permitido.')
        elif plus_saldo < 0:
            raise ValueError('este valor é negativo, não adicionado.')
        self._saldo += plus_saldo
din = ContaBancaria(100)
print(din.saldo)
din.saldo = 123
print(din.saldo)

