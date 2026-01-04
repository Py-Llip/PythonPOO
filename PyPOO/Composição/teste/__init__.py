from PyPOO.Composição.classes import Cliente

c1 = Cliente('Fellipe', 15)
c1.inserir_endereco('Curvelo', 'MG')
print(c1.nome)
c1.lista_enderecos()
del c1
print()
c2 = Cliente('Maria', 19)
c2.inserir_endereco('Brasília', 'DF')
c2.inserir_endereco('Rio de Janeiro', 'RJ')
print(c2.nome)
c2.lista_enderecos()
print()
c3 = Cliente('João', 34)
c3.inserir_endereco('Salvador', 'BA')
print(c3.nome)
c3.lista_enderecos()

print('############')