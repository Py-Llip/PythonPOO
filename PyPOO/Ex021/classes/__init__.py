'''Crie uma classe Livro com os atributos titulo, autor e ano.
 Depois, crie uma classe Biblioteca que contenha uma lista de objetos Livro. A Biblioteca deve ter métodos para:

Adicionar um livro à coleção.
Remover um livro pelo título.
Exibir todos os livros disponíveis na biblioteca.
Teste o programa criando uma biblioteca, adicionando livros e exibindo a lista de livros.'''
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.objetos_livro = []
    def add_livro(self, livro):
        for objeto in self.objetos_livro:
            if livro.titulo == objeto.titulo and livro.autor == objeto.autor and livro.ano == objeto.ano:
                self.objetos_livro.append(livro)
            else:
                print(f'O livro {livro.titulo} do autor(a) {livro.autor} feito em {livro.ano} já existe na biblioteca {self.nome}')
    def delet_livro(self, livro):
        if livro in self.objetos_livro:
            self.objetos_livro.remove(livro)
        else:
            print(f'O livro {livro.titulo} não existe na Biblioteca {self.nome}')
    def exibir_biblioteca(self):
        if self.objetos_livro:
            for e, objeto in enumerate(self.objetos_livro):
                print(f'Nº:{e+1} - {objeto.titulo} - ~{objeto.autor}~ - {objeto.ano}')
        else:
            print(f'A biblioteca {self.nome} está sem livros')

Bb = Biblioteca('Lus')
l1 = Livro('Úrsula', 'Maria Firmina', 1887)
l2 = Livro('Maneiras de Programar', 'Fellipe Alves', 2026)
Bb.add_livro(l1)
Bb.add_livro(l2)
Bb.delet_livro(l1)
Bb.exibir_biblioteca()