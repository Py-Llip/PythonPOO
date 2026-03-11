class Mat:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        if isinstance(other, (Mat, int)):
            valor = other.num if isinstance(other, Mat) else other
            return self.num + valor
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other) # reaproveita a lógica do __add__

    def __iadd__(self, other):
        if isinstance(other, (Mat, int)):
            self.num += other.num
        return self

m1 = Mat(10)
m2 = Mat(2)
print(12 + m1, m2 + m1, m1 + m2, m1 + 12) # Saída: 22 12 12 22
m1 += m2
print(m1) # Saída: 12

