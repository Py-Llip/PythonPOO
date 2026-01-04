"""### **9. Herança múltipla básica**
Crie duas classes:
- `ClasseA` com um método `metodo_a()`.
- `ClasseB` com um método `metodo_b()`.
Crie uma classe `ClasseC` que herda de ambas e possui um método que chama `metodo_a()` e `metodo_b()`."""
class ClasseA:
    def metodo_a(self):
        print('Chamando o método A!')
class ClasseB:
    def metodo_b(self):
        print('Chamando o método A!')
class ClasseC(ClasseA, ClasseB):
    def metodo_c(self):
        print('Método C chamando os métodos a e b!')
        self.metodo_a()
        self.metodo_b()
c = ClasseC()
c.metodo_c()