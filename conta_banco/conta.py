class Conta:
    def __init__(self, IN, nome, saldo):
        self.IN = IN
        self.nome = nome
        self.saldo = float(saldo)
    
    def verificar_info(self):
        print(f'IN: {self.IN}\nNome: {self.nome}\nSaldo: {self.saldo}')
    
    def deposito(self, valor):
        self.saldo += valor
        print(f'Seu saldo é de: {self.saldo}')
    
class Conta_corrente(Conta):
    def __init__(self, IN, nome, saldo):
        super().__init__(IN, nome, saldo)
        
    def sacar(self, valor):
        self.saldo -= float(valor)
        print(f'Seu saldo é de: {self.saldo}')


class Conta_poupanca(Conta):
    def __init__(self, IN, nome, saldo, juros = 0.5):
        super().__init__(IN, nome, saldo)
        self.juros = juros
        
