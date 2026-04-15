from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('José', 17, 'informatica', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'biologia', 'Mestrado')
    #inspect(p1, methods=True)
    p1.dar_aula()

    f1 = Funcionario('Claudia', 27, 'secretaria', 'secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1, methods=True)

if __name__ == '__main__':
    main()