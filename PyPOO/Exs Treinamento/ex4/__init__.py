"""Crie uma classe base chamada Animal com atributos nome e idade e um método falar() que imprime uma mensagem genérica.
Crie duas classes derivadas:

Cachorro que sobrescreve falar() para imprimir "Au au".
Gato que sobrescreve falar() para imprimir "Miau".
Teste criando instâncias das subclasses.
### **2. Adicionando métodos específicos**
Use a hierarquia do exercício anterior.
- Adicione um método específico `cavar()` em `Cachorro`.
- Adicione um método específico `pular_alto()` em `Gato`.
Teste chamar os métodos adicionais.🚀
"""
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f'O animal {self.nome} está cochichando')
class Cao(Animal):
    def falar(self):
        print(f'O animal {self.nome} está latindo: Au au!')
    def cavar(self):
        print(f'O animal {self.nome} está cavando: chuck! chuck!')
class Gato(Animal):
    def falar(self):
        print(f'O animal {self.nome} está miando: Miau!')
    def pular_alto(self):
        print(f'O animal {self.nome} está pulando: Town! Town!')
ovelha = Animal('Ovelha dentuça', 16)
gato = Gato('Gata sapeca', 5)
cao = Cao('Cadela bisonha', 17)
ovelha.falar()
gato.falar()
cao.falar()
cao.cavar()
gato.pular_alto()

