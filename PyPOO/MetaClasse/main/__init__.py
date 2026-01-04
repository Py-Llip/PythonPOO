
#Metaclasses são classes que criam outras classes, toda classe que herda de type é uma meta classe
class NameMyMetaClass(type):
    def __new__(mcs, name, bases, namespace):
        print('__new__ da metaclass')
        if name == 'Person':
            raise Exception('Cannot use name Person')
        cls = super().__new__(mcs, name, bases, namespace)
        return cls
class Person(metaclass=NameMyMetaClass):
    def __new__(cls, *args, **kwargs):
        print('__new__ da metaclass')
        return super().__new__(cls)
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
"""def init_person(self, name, lastname):
    self.name = name
    self.lastname = lastname
Person = type('Person', (), {
'__init__': init_person
})"""
print(type(Person))
person1 = Person('Luiz', 'Otávio')
person2 = Person('Maria', 'Oliveira')
print(person1.name)
print(person2.name)