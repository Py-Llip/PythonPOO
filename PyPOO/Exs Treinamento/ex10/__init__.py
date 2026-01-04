"""### **8. Inicializando listas em herança**
Crie uma classe base `Biblioteca` com uma lista de `livros` e métodos para adicionar/remover livros.
Crie uma subclasse `BibliotecaInfantil` que só permite adicionar livros apropriados para crianças."""
class Biblioteca:
    def __init__(self):
        self.lst_livros = []

    def add_livro(self, nome_livro):
        if nome_livro not in self.lst_livros:
            self.lst_livros.append(nome_livro)
            print(f'Livro: {nome_livro} adiconado com sucesso!')
        else:
            print(f'Não foi possível adicionar o livro: {nome_livro} da biblioteca. Pois já existe.')

    def del_livro(self, nome_livro):
        if nome_livro in self.lst_livros:
            self.lst_livros.remove(nome_livro)
            print(f'Livro: {nome_livro} removido da biblioteca.')
        else:
            print(f'Não foi possível remover o livro: {nome_livro} da biblioteca. Pois não existe.')

    def listar(self):
        for e, livro in enumerate(self.lst_livros):
            print(f'{e+1} Livro: {livro}')
class BibliotecaInfantil(Biblioteca):
    def add_livro(self, categoria, nome_livro=None):
        if categoria.lower().strip() in ('crianca', 'criança') and nome_livro:
            super().add_livro(nome_livro)
b1 = Biblioteca()
b1.add_livro('Harry')
b1.listar()
b2 = BibliotecaInfantil()
b2.add_livro('crianca', 'aventuras')
b2.add_livro('crianca', 'acao')
b2.del_livro('aventuras')
b2.listar()