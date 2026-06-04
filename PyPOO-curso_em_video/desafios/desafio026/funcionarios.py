from rich.panel import Panel
from rich import print
from abc import ABC, abstractmethod

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = None

    @abstractmethod
    def calcular_salario(self) -> float | int:
        pass

    def analisar_salario(self):
        painel = Panel(f'O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario / self.__class__.sal_min:.1f} salários mínimos[/].', title='Análise de Salários', width=50)
        print(painel)



class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome, None)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_salario(self) -> float | int:
        self.salario = self.valor_hora * self.qtd_horas  * (1 - self.__class__.inss / 100)
        return self.salario




class FuncionarioMensalista(Funcionario):
    def calcular_salario(self) -> float | int:
        self.salario = self.sal_bruto * (1-self.__class__.inss/100)
        return self.salario