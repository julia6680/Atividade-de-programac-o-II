'''2' Crie um sistema para um aplicativo bancário, que possui a Classe
ContaBancaria com as seguintes características:
○ Atributos: titular, saldo, numero_conta e tipo_conta.
○ Métodos: depositar, sacar, transferir e verificar_saldo.
OBS: Após cada alteração no saldo, exiba o novo valor na tela'''

class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
    def depositar(self):
        valor = float(input("Digite o valor? "))
        self.saldo += valor
        print(f"O novo saldo é : {self.saldo:.2f}")
    def sacar(self):
        saca = float(input("Digite o valor para sacar o dinheiro?  "))
        self.saldo -= saca
        print(f"O novo saldo é {self.saldo:.2f}")
    
    def transferir(self,saldo_de_julia):
        valor = float(input("Digite o valor para transferir:  "))
        self.saldo -= valor
        saldo_de_julia += valor
        print(f'o saldo de fuluana é {saldo_de_julia} ') 
    def verificar_saldo(self):
        print(f"O saldo é:{self.saldo}")
        

julia = ContaBancaria("melhor do mundo",1000.90,"32-0","CC")
ana = ContaBancaria("amen",9000.02,"6575-0","cp")
julia.depositar()
ana.sacar()
julia.saldo = ana.transferir(julia.saldo)
julia.verificar_saldo()

