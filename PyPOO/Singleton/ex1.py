"""
Entendido! Aqui estão três exercícios específicos para Python orientado a objetos, focados no padrão de projeto Singleton.

Exercício 1: Singleton Básico
Implemente uma classe Singleton em Python. Esta classe deve:

Usar o método especial __new__ para garantir que apenas uma instância da classe seja criada.
Possuir um método estático get_instance que retorne a única instância.
Instruções
Crie a classe Singleton usando o método __new__.
Adicione o método get_instance para obter a única instância.
Teste sua implementação criando múltiplos objetos e verificando se todos apontam para a mesma instância."""
class Singleton:
    _instancia = None
    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    @staticmethod
    def get_instance():
        if not Singleton._instancia:
            Singleton._instancia = Singleton()
        return Singleton._instancia
a = Singleton().get_instance()
b = Singleton().get_instance()
print(a is b)
