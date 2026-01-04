from abc import ABC, abstractmethod
class Film(ABC):
    name = None
    price_base = None
    @abstractmethod
    def return_price_daily(self):
        pass
"""    def teste(self):
        return print('ativo')"""