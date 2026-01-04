"""### **6. Chamando o método da classe base**
Crie uma classe base `Funcionario` com um método `trabalhar()` que imprime "Trabalhando!".
Crie uma classe derivada `Gerente` que sobrescreve o método para adicionar "Supervisionando!".
No método sobrescrito, chame o método da classe base usando `super()`."""
#base
class Funcionario:
    def trabalhar(self):
        print('Trabalhando!')
#derivada
class Gerente(Funcionario):
    def trabalhar(self):
        print('Supervisionando!')
        super().trabalhar()
funcionario = Funcionario()
funcionario.trabalhar()
gerente = Gerente()
gerente.trabalhar()