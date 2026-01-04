'''Crie uma classe Pessoa que tenha um atributo de classe contador,
que conta o número de instâncias criadas.
Cada vez que uma nova pessoa for criada, incremente esse contador.
Implemente um método de classe chamado contar_pessoas() que retorna o número total de pessoas criadas.'''
from PyPOO.Ex005.classes import Pessoa
p1 = Pessoa(nome='Fellipe', sexo='M')
print(p1.contar_pessoas())
