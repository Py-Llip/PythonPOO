class MeusBytes:
    def __init__(self, texto):
        self.texto = texto

    def __bytes__(self):
        return bytes(self.texto, encoding='utf-8')

l = MeusBytes('Olá')
print(bytes(l))