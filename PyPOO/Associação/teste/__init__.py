from PyPOO.Associação.classes import Escritor
from PyPOO.Associação.classes import Caneta
from PyPOO.Associação.classes import MaquinaDeEscrever

escritor = Escritor('Fellipe')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()