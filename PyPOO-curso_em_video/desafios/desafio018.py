from rich.panel import Panel
from rich import print
class Churrasco:
    def __init__(self, titulo, qnt_pessoas):
        self.qnt = qnt_pessoas
        self.titulo = titulo
    def analisar(self, consumo=400, preco=82.40):
        consumo = consumo / 1000
        custo_total = self.qnt * consumo * preco
        texto = f'''Analisando [green]{self.titulo}[/] com [blue]{self.qnt} convidados[/]
Cada participante comerá {consumo}Kg e cada Kg custa R${preco:.2f}
Recomendo [blue]comprar {self.qnt * consumo:.3f}Kg[/] de carne
O custo total será de [green]R${custo_total:.2f}[/]
Cada pessoa pagará [yellow]R${custo_total / self.qnt:.2f}[/] para participar.'''
        painel = Panel(texto, title=self.titulo)
        print(painel)

c1 = Churrasco('Churrasco dos Amigos', 15)
c1.analisar()
