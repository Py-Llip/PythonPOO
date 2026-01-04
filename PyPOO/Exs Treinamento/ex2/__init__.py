'''Crie uma classe base `Pessoa` com um atributo protegido `_idade`. Crie uma classe derivada `Aluno` que acessa e imprime a idade da pessoa.

**Explicação:**
Introduz o conceito de atributos protegidos e como eles são acessados em classes derivadas.'''
class Pessoa:
    def __init__(self, idade):
        self._idade = idade
class Aluno(Pessoa):
    def idade(self):
        return self._idade
p1 = Aluno(15)
print(p1.idade())

