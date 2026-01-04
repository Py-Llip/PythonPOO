altura = int(input("Digite a altura do triângulo retângulo: "))
base = int(input("Digite a base do triângulo retângulo: "))
for i in range(1, altura + 1):
    largura = round((i / altura) * base)
    print('*  ' * largura)