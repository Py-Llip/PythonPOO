from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome:str='Sem nome', preco:float|int=0):
        self.nome = nome
        self.preco = float(preco)

    def etiqueta(self):
        width = 35
        for e, n in enumerate(range(len(spreco := str(self.preco).split('.')[0])-1, -1, -1)):
            if e % 3 == 0 and e > 1:
                spreco = spreco[:n+1] + '.' + spreco[n+1:]

        preco = 'R$' + spreco + ',' + f'{self.preco:.2f}'.split('.')[1]
        conteudo = f'{self.nome: ^{width-4}}\n{"-"*(width-4)}\n{preco:.^{width-4}}'
        etiqueta = Panel(title='Produto', renderable=conteudo, style='#ffdd33', width=width)
        print(etiqueta)

Produto('Borracha', 2).etiqueta()
Produto('Celular', 7_000_000).etiqueta()