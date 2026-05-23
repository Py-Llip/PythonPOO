from abc import ABC, abstractmethod
from random import randint, choice
from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = ['Tapa']

    def atacar(self, alvo, forca:int):
        forca_nova = randint(0, forca)
        print(f'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{choice(self.golpes)}[/] de força [cyan]{forca}[/]')
        alvo.receber_dano(dano=forca_nova)


    def receber_dano(self, dano):
        self.vida -= dano
        print(f'[blue]{self.nome}[/] recebeu [red]dano de {dano}[/]!')

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Pulo Giratório', 'Golpe de Machado']
    def curar(self):
        cura = randint(0, 50)
        self.vida += cura
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]recuperou {cura} pontos[/] de vida')

class Mago(Personagem):
    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        print(f'[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida')