class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def __str__(self):
        class_str = f'{self.__class__.__name__}' \
        f'({self.name} {self.lastname})'
        return class_str

if __name__ == '__main__':
    john = Person('John', 'Doe')
    print(john)