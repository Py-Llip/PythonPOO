from frete import *
from rich import print
from rich.table import Table

def main():
    dist = 50

    entrega = [Moto(dist), Caminhao(dist), Drone(dist)]
    a = Table('Distância', 'Tipo', 'Frete', title='Tabela de Fretes')
    for n in range(3):
        a.add_row(f'{entrega[n].distancia}Km', type(entrega[n]).__name__, entrega[n].calc_frete())
    print(a)
    #print(f'Frete  de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}')

if __name__ == '__main__':
    main()