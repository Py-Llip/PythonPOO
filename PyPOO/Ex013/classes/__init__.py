class Produto:
    produto_dic = dict()
    def __init__(self, nome, preco, quant_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quant_estoque = quant_estoque
        Produto.produto_dic[self.__nome]= {
            'preço': self.__preco,
            'quantidade': self.__quant_estoque
        }

    def novo_preco(self, novo_preco):
        if novo_preco > 0:
            Produto.produto_dic[self.__nome]['preço'] = novo_preco
        else:
            raise ValueError(f'O {novo_preco} tem que ser maior que 0')
    @classmethod
    def consulta_produto(cls, nome_produto):
        cls.linha()
        print(f'{"TABELA":*^30}')
        cls.linha()
        print(f'{'('+nome_produto+')':^30}')
        for chave, valor in cls.produto_dic[nome_produto].items():
            print(f'{chave:<15}{valor:>15}')


    @staticmethod
    def linha():
        print('-'*30)

    def addorremov(self, valor):
        if Produto.produto_dic[self.__nome]['quantidade'] + valor >= 0:
            Produto.produto_dic[self.__nome]['quantidade'] += valor
        else:
            raise ValueError(f'O valor {valor} não é compatível com este método')


p1 = Produto('Feijão', 5.5, 2)
p1.consulta_produto('Feijão')
p1.addorremov(10)
p1.novo_preco(50)
p1.consulta_produto('Feijão')
