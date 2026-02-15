from rich import print
from time import sleep
class Livro:
    def __init__(self, titulo:str='Desconhecido', paginas:int=10):
        self.titulo = titulo
        self.paginas = paginas
        self.total = 1
        print(f':book:[blue]Você acabou de abrir "[red]{self.titulo}[/]" que tem [green]{self.paginas} páginas[/] no total. Você está na [yellow]página 1[/][/]')

    def avancar_paginas(self, paginas:int=0):
        final = False
        if (resto := self.paginas - self.total) <= paginas :
            paginas = resto
            final = True

        for p in range(self.total, self.total + paginas):
            print(f'Pág{p+1} :play_button: ', end='')
            sleep(0.5)

        self.total += paginas
        print(f'[blue]Você avançou {paginas} páginas e agora está na [/][yellow]página {self.total}[/]')
        print(f':books: Você chegou ao final do livro "[red]{self.titulo}[/]".') if final == True else None
        return self

l1 = Livro()
l1.avancar_paginas(5).avancar_paginas(2)
l1.avancar_paginas(1)