"""Exercício 2: Herança Múltipla e Métodos com Parâmetros
Descrição: Crie duas classes base chamadas Computador e Celular. A classe Computador deve ter um método ligar() que imprime "Computador ligado".
 A classe Celular deve ter um método ligar() que imprime "Celular ligado". Depois, crie uma classe derivada chamada SmartPC,
  que herda de ambas as classes Computador e Celular, e sobrescreve o método ligar() para fazer algo mais complexo, como imprimir "SmartPC ligado,
   configurando ambos os sistemas."

Passos:

Crie a classe Computador com o método ligar().
Crie a classe Celular com o método ligar().
Crie a classe SmartPC que herda de Computador e Celular e sobrescreve ligar().
Chame super() para invocar o método das classes base, e depois faça o comportamento avançado na classe derivada.
Instancie um objeto de SmartPC e teste o método ligar()."""
class Computador:
    def ligar(self):
        print('Computador ligando')
class Celular:
    def ligar(self):
        print('Celular ligando')
class SmartPC(Computador, Celular):
    def ligar(self):
        super().ligar()
        Celular.ligar(self)
        print('SmartPC ligando, configurando ambos os sistemas')
s = SmartPC()
s.ligar()
