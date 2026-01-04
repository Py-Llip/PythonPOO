"""### **7. Encapsulamento e herança**
Crie uma classe `ContaBancaria` com atributos privados `_saldo` e métodos `depositar()` e `sacar()`.
Crie uma subclasse `ContaCorrente` que adiciona um limite de saque."""
class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
    def depositar(self, valor):
        self._saldo += valor
    def sacar(self, valor):
        self._saldo -= valor
    def exibir_saldo(self):
        print(self._saldo)
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if valor <= 500:
            self._saldo -= valor
        else:
            print('Não foi possível realizar o saque pois o limite máximo é de 500 ou menos.')
contabancaria = ContaBancaria(1000)
contacorrente = ContaCorrente(1000)
contabancaria.depositar(500)
contabancaria.exibir_saldo()
contabancaria.sacar(1000)
contabancaria.exibir_saldo()
contacorrente.depositar(500)
contacorrente.exibir_saldo()
contacorrente.sacar(1000)
contacorrente.exibir_saldo()
contacorrente.sacar(500)
contacorrente.exibir_saldo()
