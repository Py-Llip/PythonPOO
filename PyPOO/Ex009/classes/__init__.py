class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if not isinstance(new_celsius, (float, int)):
            raise TypeError('o tipo de celsius não é considerado um número inteiro ou float.')
        self._celsius = new_celsius

    def fahrenheit(self):
        return self._celsius * 1.8 + 32

temp = Temperatura(10)
print(temp.fahrenheit())
temp.celsius = 30
print(temp.fahrenheit())
print(temp.celsius)
temp.celsius = 'quente'