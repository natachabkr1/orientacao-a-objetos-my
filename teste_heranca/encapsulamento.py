# Encapsulamento - criar um método dentro da classe- Exe. def sacar

class ContaBancaria:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.__numero = numero           # Atributo privado
        self.__titular = titular         # Atributo privado
        self.__saldo = saldo_inicial     # Atributo privado
    
    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia     #adiciona o valor ao saldo
            return f"Depósito de R${quantia} realizado com sucesso. Saldo atual: R${self.__saldo}"
        else:
            return "Quantia de depósito inválida."

    def sacar(self, quantia):
        if 0 < quantia <= self.__saldo:
            self.__saldo -= quantia   # subtrai o valor do saldo
            return f"Saque de R${quantia} realizado com sucesso. Saldo atual: R${self.__saldo}"
        else:
            return "Saldo insuficiente ou quantia inválida."

    def consultar_saldo(self):
        return f"Saldo atual: R${self.__saldo}"

    def get_numero_conta(self):    # Método getter para acessar o número da conta
        return self.__numero

# Criando uma conta bancária
conta = ContaBancaria(123456, "João Silva", 1000)

# Realizando operações
print(conta.depositar(500))  # Depósito realizado
print(conta.sacar(200))      # Saque realizado
print(conta.consultar_saldo()) # Consulta de saldo

# Tentativa de acessar atributos privados diretamente (não recomendado)
# print(conta.__saldo)  # Isso geraria um erro AttributeError
