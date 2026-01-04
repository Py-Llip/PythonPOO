"""### **5. Polimorfismo em ação**
Crie uma classe base `Forma` com um método `area()` que retorna 0.
Crie duas subclasses:
- `Retangulo` com atributos `largura` e `altura`.
- `Circulo` com atributo `raio`.
Implemente o método `area()` em cada subclasse para calcular a área correta.
"""
class Forma:
    def area(self):
        return 0
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio ** 2
losango = Forma().area()
retangulo = Retangulo(5, 5).area()
circulo = Circulo(5).area()
print(losango, retangulo, circulo)

