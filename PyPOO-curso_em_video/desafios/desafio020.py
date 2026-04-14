from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome:str='Desconhecido', nick:str='Desconhecido'):
        self.nome = nome
        self.nick = nick
        self.lis_fav = []

    def add_favoritos(self, game: str):
        self.lis_fav.append(f':video_game: {game}')
        self.lis_fav = sorted(self.lis_fav, key=str.lower)

    def ficha(self):
        print(Panel(f'Nome real: [black on white]{self.nome}[/]\nJogos favoritos:\n[blue]{"\n".join(self.lis_fav)}[/]', title=f'Jogador <{self.nick}>'))

g1 = Gamer('Fellipe', 'llippok')
g1.add_favoritos('Roblox')
g1.add_favoritos('Brawl Stars')
g1.add_favoritos('Minecraft')
g1.ficha()