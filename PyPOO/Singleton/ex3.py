"""Exercício 3: Singleton com Thread Safety
Implemente uma versão thread-safe do Singleton, garantindo que múltiplas threads não criem instâncias separadas.

Instruções
Use o módulo threading para simular um ambiente multithread.
Proteja o método get_instance com um bloqueio (threading.Lock) para garantir que apenas uma thread possa criar a instância.
Desafio Extra
Crie múltiplas threads tentando acessar o método get_instance ao mesmo tempo e verifique se apenas uma instância é criada."""
#versão thread-safe
import threading
