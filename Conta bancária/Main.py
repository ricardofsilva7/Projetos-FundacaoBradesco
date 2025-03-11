class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1= Cliente("Vinicius Pires", "1199606-0610")
conta=Conta(c1.get_nome(), 1222)

conta.deposito(100)
conta.saque(50)
conta.extrato()
