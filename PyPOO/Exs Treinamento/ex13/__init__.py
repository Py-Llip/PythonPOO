"""Exercício Avançado: Herança, Sobrescrita e Métodos com Parâmetros
Descrição:
Crie uma classe base chamada Veiculo com o método ligar() que aceita um parâmetro modo (que pode ser "normal" ou "eco").
 Dependendo do valor de modo, o comportamento de "ligar" será diferente. Em seguida, crie duas classes derivadas: Carro e Caminhao.
  Ambas as classes devem sobrescrever o método ligar() e adicionar um comportamento específico com base no tipo de veículo e o parâmetro modo.
   Utilize a função super() para invocar o método ligar() da classe base e, dentro das classes derivadas, personalizar ainda mais o comportamento de "ligar".

Passos:
Crie a classe base Veiculo com um método ligar() que aceita o parâmetro modo.
Crie as classes Carro e Caminhao, que herdam de Veiculo e sobrescrevem o método ligar().
Nos métodos das classes derivadas, adicione lógicas diferentes com base no parâmetro modo, como "Carro ligado no modo normal" ou "Caminhão ligado no modo eco".
Utilize super() para chamar o método ligar() da classe base e personalize ainda mais o comportamento nas classes derivadas."""
class Veiculo:

    def ligar(self, modo='normal'):
        if modo.lower().strip() in ['normal']:
            print('Modo normal ligado com sucesso!')
        elif modo.lower().strip() in ['eco']:
            print('Modo eco ligado com sucesso!')
        else:
            print("Erro! Não existe este modo, use 'normal' ou 'eco'.")
class Carro(Veiculo):
    def ligar(self, modo='normal'):
        print(f'Ligando o Carro no modo {modo.lower().strip()}:')
        super().ligar(modo)
        if modo.lower().strip() == 'eco':
            print('Carro na economia máxima!')
        elif modo.lower().strip() == 'normal':
            print(f'Carro com a maior Potência!')
class Caminhao(Veiculo):
    def ligar(self, modo='normal'):
        print(f'ligando o caminhão no modo {modo.lower().strip()}:')
        super().ligar(modo)
        if modo.lower().strip() == 'eco':
            print('Caminhão com o menos desperdício!')
        elif modo.lower().strip() == 'normal':
            print(f'Caminhão com a maior velocidade!')
veiculo = Veiculo()
veiculo.ligar()
carro = Carro()
carro.ligar()
caminhao = Caminhao()
caminhao.ligar()



