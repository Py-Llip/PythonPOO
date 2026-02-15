from rich import print
from rich.panel import Panel
class ControleRemoto:
    def __init__(self):
        self.canal = 1
        print(self.canal)
        self.volume = 1
        self.ativa = False
        self.alerta = ''

    def ligar(self):
        if not self.ativa:
            texto = ':prohibited: [red]A TV está desligada[/]'
        else:
            texto = f'CANAL  = {self.__set_canal()} \nVOLUME = {self.__set_volume()}'

        p = Panel(texto, title='[ TV ]', width=33)
        print(p)

    def __set_volume(self):
        volume = ''
        if self.volume < 0:
            self.volume = 0
        elif self.volume > 6:
            self.volume = 6

        for v in range(6):
            cor = 'white'
            if v+1 <= self.volume:
                cor = 'blue'
            volume += f'[on {cor}] [/]'
        return volume

    def __set_canal(self):
        canal = ''
        if self.canal > 5:
            self.canal = 1
        elif self.canal < 1:
            self.canal = 5
        for n in range(5):
            if n+1 == self.canal:
                canal += f'[on yellow] {self.canal} [/]'
                continue
            canal += f' {n+1} '
        return canal

    def geren_btn(self):
        btn = input('< CH1 >  |  - VOL2 + : ')
        if btn in ['@', '0'] or self.ativa:
            match btn:
                case '@':
                    self.ativa = True if not self.ativa else False
                    return None
                case '-':
                    self.volume -= 1
                    return None
                case '+':
                    self.volume += 1
                    return None
                case '<':
                    self.canal -= 1
                    return None
                case '>':
                    self.canal += 1
                    return None
                case '0':
                    return False
                case _:
                    self.alerta = f'O botão {btn} não corresponde a nenhum outro.'
                    return None
        self.alerta = f'O botão {btn} não corresponde a nenhum outro.'
        return None

    def inicializar(self):
        estado = None
        while estado is not False:
            self.ligar()
            estado = self.geren_btn()
            print('\n' * 20)
            print(self.alerta)
            self.alerta = ''


c = ControleRemoto()
c.inicializar()