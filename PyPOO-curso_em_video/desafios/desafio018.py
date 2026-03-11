from rich.panel import Panel
from rich import print
class Churrasco:
    consumo_padrao:float = 0.400 # 400 gramas
    preco_kg:float = 82.40 # cada Kg de carne custa esse valor em reais
    def __init__(self, titulo, qnt_pessoas):
        self.qnt = qnt_pessoas
        self.titulo = titulo
    def analisar(self):
        texto = f'''Analisando [green]{self.titulo}[/] com [blue]{self.qnt} convidados[/]
Cada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:.2f}
Recomendo [blue]comprar {self.qnt * Churrasco.consumo_padrao:.3f}Kg[/] de carne
O custo total será de [green]R${self.__class__.preco_kg * Churrasco.consumo_padrao * self.qnt:.2f}[/]
Cada pessoa pagará [yellow]R${Churrasco.preco_kg * Churrasco.consumo_padrao:.2f}[/] para participar.'''
        painel = Panel(texto, title=self.titulo)
        print(painel)

c1 = Churrasco('Churrasco dos Amigos', 30)
c1.analisar()
