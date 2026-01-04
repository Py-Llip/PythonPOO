"""Exercício 2: Sistema de Contas Bancárias
Implemente uma classe abstrata chamada ContaBancaria com os seguintes métodos abstratos:

depositar(valor)
sacar(valor)
consultar_saldo()
Crie duas subclasses concretas:

ContaCorrente: permite sacar até o saldo disponível.
ContaPoupanca: não permite saques caso o saldo fique negativo.
Teste os métodos de cada tipo de conta."""
import abc
class ContaBancaria(abc.ABC):
    def __init__(self,  saldo):
        self.saldo = saldo
    @abc.abstractmethod
    def depositar(self, valor):
        pass
    @abc.abstractmethod
    def sacar(self, valor):
        pass
    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo}')
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Não é possível sacar este valor, saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Operação finalizada com sucesso! Saldo atual: R${self.saldo}')
    def depositar(self, valor):
        self.saldo += valor
class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if self.saldo < 0:
            print(f'Não foi possível realizar esta operação pois sua conta está negativa.')
        else:
            self.saldo -= valor
            print(f'Operação finalizada com sucesso! Saldo atual: R${self.saldo}')
    def depositar(self, valor):
        self.saldo += valor
cc = ContaCorrente(100)
cb = ContaPoupanca(12)
cc.consultar_saldo()
cc.sacar(20)
cc.consultar_saldo()

