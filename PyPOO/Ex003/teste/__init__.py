'''Crie uma classe Carro que tenha um atributo de classe carros_registrados
(uma lista). Cada vez que um novo carro for criado, adicione o carro à lista.
Implemente um método de classe chamado mostrar_carros() que exibe todos os carros registrados.'''
from PyPOO.Ex003.classes import Carro
Lamborguini = Carro('lamborguini')
Ferrari = Carro('Ferrari')
Carro.mostrar_carros()