from PyPOO.AbstracaoClassesAbstratas.Film import *

class Normal(Film):
    def __init__(self, name, price_base):
        Film.name = name
        Film.price_base = price_base
    def return_price_daily(self):
        return self.price_base


