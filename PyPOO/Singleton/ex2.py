"""Exercício 2: Propriedade Compartilhada no Singleton
Adicione uma funcionalidade à classe Singleton para compartilhar propriedades. Por exemplo:

Crie uma propriedade contador com valor inicial 0.
Adicione métodos incrementar e obter_contador para manipular e acessar o valor de contador.
Instruções
Expanda o Singleton criado no Exercício 1.
Teste se incrementos na propriedade contador de um objeto afetam todos os objetos (porque é a mesma instância)."""
class Singleton:
    _instancia = None
    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    def __init__(self):
        if not hasattr(self, 'contador'):
            self.contador = 0
    def adicionar(self, valor):
        self.contador += valor
    def exibir_valor(self):
        print(f'O valor é {self.contador}')
obj1 = Singleton()
obj2 = Singleton()
obj2.adicionar(4)
obj1.adicionar(5)
obj1.exibir_valor()
obj2.exibir_valor()
