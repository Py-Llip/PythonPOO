class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = list()

    def adicionar(self, livro):
        if livro not in self.livros:
            self.livros.append(livro)
            print(f'O livro {livro.titulo} foi adicionado a Biblioteca')
        else:
            raise ValueError(f'Não foi possível adicionar o livro {livro.titulo}, pois já é existente.')

    def listar(self):
        print(f'BIBLIOTECA {self.nome}')
        for livro in self.livros:
            print(f'{livro.titulo} - {livro.autor}')

livro1 = Livro('As aventuras de Harry Potter', 'Harry Potter')
livro2 = Livro('Homem de Ferro', 'Jack P.')
bbtc = Biblioteca('Central')
bbtc.adicionar(livro2)
bbtc.adicionar(livro1)
bbtc.listar()