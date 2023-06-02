class ContaBancaria:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque Realizado com Sucesso!!!")
        else:
            print("Saldo Insuficiente para Realizar o Saque!!!")

    def exibir_saldo(self):
        print(f"Saldo Disponível na Conta {self.numero_conta}: R${self.saldo}")


class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque Realizado com Sucesso!!!")
        else:
            print("Saldo Insuficiente!!!")

    def exibir_saldo(self):
        print(f"Saldo Disponível na Conta Corrente {self.numero_conta}: R${self.saldo}")


class ContaPoupanca(ContaBancaria):
    def calcular_juros(self, taxa):
        juros = self.saldo * (taxa / 100)
        self.saldo += juros
        print(f"Juros de R${juros} Calculados e Cdicionados!!!")


contas = [ContaBancaria("222", 2000), ContaCorrente("555", 3000), ContaPoupanca("777", 7000)]


for conta in contas:
    conta.sacar(260)
    conta.exibir_saldo()
    print("="*40)