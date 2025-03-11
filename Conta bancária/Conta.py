class Conta:
    def __init__(self, titular, numero):
        self._saldo=0.0
        self._numero=numero
        self._titular=titular

    
    #metodo get
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    #metodo set
    def saldo(self, saldo):
        if (saldo<0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo-= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo Insuficiente")

    def deposito(self, valor):
        self.saldo+=valor
        print("Deposito realizado com suecesso.")

    def extrato(self):
        print("Cliente: ", self._titular, "Seu saldo: ", self._saldo)