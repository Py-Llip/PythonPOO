class Classe:
    LISTA_VIDA = [70, 100, 120]
    LISTA_CLASSE = ['Elfo', 'Guerreiro', 'Lutador']
    TUPLA_ATAQUE1 = (['Vara', 'Espada', 'Soco'], {
        'Vara': '25',
        'Espada': '45',
        'Soco': '20'})
    TUPLA_ATAQUE2 = (['CadeiaDeRaiz', 'CoragemAfiada', 'MovimentosNãoVisíveis'], {
        'CadeiaDeRaiz': ('12 * segundo durante 15 s', '12 + segundo de cura durante 8 s'),
        'CoragemAfiada': ('80', '20 de vida a menos'),
        'MovimentosNãoVisíveis': ('13 * 2/segundo durante 30 s', '40% de fraqueza durante 20 s')
    })
    @classmethod
    def elfo(cls):
        return 0

    @classmethod
    def guerreiro(cls):
        return 1

    @classmethod
    def lutador(cls):
        return 2

class Personagem:
    def __init__(self, nome: str, idade: int, classe: Classe):
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.vida = Classe.LISTA_VIDA[self.classe]
        self.vida_atual = self.vida

    def get_vida(self):
        return self.vida_atual

    def tabela_personagem(self):
        dic_tabela = {
            'Nome': self.nome,
            'Idade': self.idade,
            'Classe': Classe.LISTA_CLASSE[self.classe],
            'Vida': self.vida,
            'Vida Atual': self.get_vida(),
            'Primeiro ataque': f'{Classe.TUPLA_ATAQUE1[0][self.classe]} | {Classe.TUPLA_ATAQUE1[1][Classe.TUPLA_ATAQUE1[0][self.classe]]}',
            'Segundo ataque': f'{Classe.TUPLA_ATAQUE2[0][self.classe]} | {Classe.TUPLA_ATAQUE2[1][Classe.TUPLA_ATAQUE2[0][self.classe]][0]} COM {Classe.TUPLA_ATAQUE2[1][Classe.TUPLA_ATAQUE2[0][self.classe]][1]}'
        }
        print(f'PERSONAGEM:')
        for k, c in dic_tabela.items():
            print(f'- {k}: {c}.')

    @classmethod
    def lutar(cls, segundo_personagem, ataque):
        dano = Classe.TUPLA_ATAQUE1[1][ataque.title().strip()]
        segundo_personagem.vida_atual -= int(dano)
        print(f'Vida do adversário {segundo_personagem.nome} depois do ataque: {segundo_personagem.vida_atual} de vida')



p1 = Personagem('Fel', 21, classe=Classe.elfo())
p2 = Personagem('Mat', 34, classe=Classe.guerreiro())
p2.tabela_personagem()
p1.tabela_personagem()
p1.lutar(p2, 'Vara')
p2.lutar(p1, 'Espada')
p1.tabela_personagem()