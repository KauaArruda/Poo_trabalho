class Conta:
    def __init__(self, numero_conta, saldo_inicial):
        self.__numero_conta = numero_conta
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo Insuficiente!!!")

    def verificar_saldo(self):
        return self.__saldo


conta = Conta("1057", 1000)

print(conta.verificar_saldo())

conta.depositar(130)
print(conta.verificar_saldo())

conta.sacar(55)
print(conta.verificar_saldo())

conta.sacar(300)