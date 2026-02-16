"""são métodos que têm dois underscores no início e no final se fala dander coisa, ex dander init
__init__: inicializa os atributos.
__new__: Personalizar a criação de um objeto Chamado antes de __init__. Usado para controle avançado de criação de instâncias.
__del__: Executa ações ao deletar o objeto.
__str__: transforma a classe em um str do seu desejo.
__repr__: Representação técnica do objeto.
__format__: Permite que você passe "instruções" (como .2f) dentro de chaves {} para formatar os atributos internos.
__bytes__: Transforma o estado do objeto em uma sequência de bytes puramente técnica.


__len__: facilita o tamanho do objeto (usa-se mais nas listas)

__add__: soma uma classe com a outra
__getitem__: retorna o elemento da alista interna, ou no for n in
__setitem__: Permite modificar itens diretamente Usado para definir itens em um objeto, como se fosse um dicionário ou lista.
__bool__: retorna True ou False
__mul__: multiplica
__delitem__: remove a lista ou oq vc quer com o del
__reversed__: inverte a lista
__eq__: se colocar classe é igual a outraclasse e returna o valor da sua preferencia
__iter__: Faz a classe iterável
__call__: Torna o objeto chamável, Permite que um objeto funcione como uma função.
__contains__: Verificar se um elemento está presente, operador in
__hash__: Torna o objeto hashable

__pow__: Eleva um objeto a uma potência
__sub__: Subtração entre objetos
__lt__, __le__, __gt__, __ge__: Comparações entre objetos Permite usar <, <=, >, >=.

__getattr__ e __setattr__: Controle de atributos dinâmicos
"""
#__init__:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Fellipe", 15)
print(p.nome, p.idade)  # Saída: Fellipe 15

#__new__:
class Singleton:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Saída: True


#__del__:
class Arquivo:
    def __init__(self, nome):
        self.nome = nome
        print(f"Abrindo arquivo {nome}.")

    def __del__(self):
        print(f"Fechando arquivo {self.nome}.")

arquivo = Arquivo("dados.txt")
del arquivo  # Saída: Fechando arquivo dados.txt

#__str__:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos.'

p = Pessoa("Fellipe", 15)
print(str(p))  # Saída: Fellipe tem 15 anos.

#__repr__:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

p = Pessoa("Fellipe", 15)
print(repr(p))  # Saída: Pessoa(nome='Fellipe', idade=15)

#__format__:
class Numero:
    def __init__(self, num):
        self.num = num

    def __format__(self, format_spec):
        if format_spec == 'moeda':
            return f"R$ {self.num:,.2f}"
        return 'Não encontrado'

n = Numero(100_000_000)
print(f'{n:moeda}') # Saída: Meu dinheiro: R$ 100,000,000.00

#__bytes__:
class MeusBytes:
    def __init__(self, texto):
        self.texto = texto

    def __bytes__(self):
        return bytes(self.texto, encoding='utf-8')

l = MeusBytes('Olá')
print(bytes(l)) # Saída: b'Ol\xc3\xa1'

#__len__:
class MinhaLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

lista = MinhaLista([1, 2, 3, 4])
print(len(lista))  # Saída: 4


#__add__:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __add__(self, outra_pessoa):
        return f'{self.nome} e {outra_pessoa.nome} têm uma amizade incrível!'

p1 = Pessoa("Fellipe", 15)
p2 = Pessoa("Bianca", 14)
print(p1 + p2)

#__getitem__:
class MinhaLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

lista = MinhaLista([10, 20, 30])
print(lista[1])  # Saída: 20
for n in lista:
    print(n)  # Saída: 10 20 30

#__bool__:
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __bool__(self):
        return bool(self.nome)

p = Pessoa("")
print(bool(p))  # Saída: False

#__mul__:
class Repetidor:
    def __init__(self, texto):
        self.texto = texto

    def __mul__(self, vezes):
        return self.texto * vezes

r = Repetidor("Oi! ")
print(r * 3)  # Saída: Oi! Oi! Oi!

#__delitem__:
class MinhaLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __delitem__(self, indice):
        del self.elementos[indice]

lista = MinhaLista([10, 20, 30])
del lista[1]
print(lista.elementos)  # Saída: [10, 30]

#__reversed__:
class MinhaLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __reversed__(self):
        return reversed(self.elementos)

lista = MinhaLista([1, 2, 3])
print(list(reversed(lista)))  # Saída: [3, 2, 1]

#__eq__:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outra_pessoa):
        return self.idade == outra_pessoa.idade

p1 = Pessoa("Fellipe", 15)
p2 = Pessoa("Bianca", 15)
print(p1 == p2)  # Saída: True

#__iter__:
class MinhaLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __iter__(self):
        return iter(self.elementos)

lista = MinhaLista([1, 2, 3])
for n in lista:
    print(n)  # Saída: 1 2 3

#__call__:
class Soma:
    def __call__(self, a, b):
        return a + b

somar = Soma()
print(somar(3, 4))  # Saída: 7

#__setitem__:
class MinhaLista:
    def __init__(self):
        self.itens = {}

    def __setitem__(self, chave, valor):
        self.itens[chave] = valor

    def __getitem__(self, chave):
        return self.itens[chave]

lista = MinhaLista()
lista['a'] = 10
print(lista['a'])  # Saída: 10

#__contains__:
class MinhaLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __contains__(self, item):
        return item in self.elementos

lista = MinhaLista([1, 2, 3])
print(2 in lista)  # Saída: True

#__hash__:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __hash__(self):
        return hash((self.nome, self.idade))

p = Pessoa("Fellipe", 15)
dicionario = {p: "Estudante"}
print(dicionario)  # Saída: {Pessoa(nome='Fellipe', idade=15): 'Estudante'}

#__pow__:
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __pow__(self, potencia):
        return self.valor ** potencia

n = Numero(2)
print(n ** 3)  # Saída: 8

#__sub__:
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __sub__(self, outro):
        return self.valor - outro.valor

a = Numero(10)
b = Numero(3)
print(a - b)  # Saída: 7

#__lt__, __le__, __gt__, __ge__: <, <=, >, >=.
class Pessoa:
    def __init__(self, idade):
        self.idade = idade

    def __lt__(self, outra_pessoa):
        return self.idade < outra_pessoa.idade

p1 = Pessoa(15)
p2 = Pessoa(20)
print(p1 < p2)  # Saída: True

#__getattr__ e __setattr__:
class Pessoa:
    def __setattr__(self, nome, valor):
        print(f"Definindo {nome} como {valor}")
        self.__dict__[nome] = valor

    def __getattr__(self, nome):
        print(f"Tentando acessar {nome}")
        return "Atributo não encontrado"

p = Pessoa()
p.nome = "Fellipe"  # Saída: Definindo nome como Fellipe
print(p.sobrenome)  # Saída: Tentando acessar sobrenome
