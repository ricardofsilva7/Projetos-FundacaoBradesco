# Projeto: Desenvolvimento Orientado a Objetos em Python

## Descrição
Este repositório contém um projeto desenvolvido durante o curso **Desenvolvimento Orientado a Objetos Utilizando a Linguagem Python**. O objetivo principal foi aplicar conceitos fundamentais da Programação Orientada a Objetos (POO), utilizando Python como linguagem de implementação.

## Conceitos abordados
Durante o desenvolvimento deste projeto, foram aplicados os seguintes conceitos:
- **Método Construtor (`__init__`)**
- **Encapsulamento** (uso de atributos protegidos `_atributo`)
- **Métodos Get e Set (`@property` e `@setter`)**
- **Método `len()`**
- **Funções e Manipulação de Objetos**

## Estrutura do Código
O projeto consiste em três classes principais:

### Classe `Cliente`
Representa um cliente bancário, contendo informações básicas como nome e telefone. Implementa o conceito de **encapsulamento**, utilizando métodos get e set para manipular os atributos protegidos.

```python
class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
```

### Classe `Conta`
Representa uma conta bancária, com funcionalidades para **depósito**, **saque** e **visualização de extrato**. Utiliza **propriedades (`@property`)** para controlar o saldo da conta.

```python
class Conta:
    def __init__(self, titular, numero):
        self._saldo = 0.0
        self._numero = numero
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo Insuficiente")

    def deposito(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso.")

    def extrato(self):
        print("Cliente:", self._titular, "Seu saldo:", self._saldo)
```

### Classe `Main`
Responsável por inicializar e testar as funcionalidades do sistema bancário.

```python
from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Vinicius Pires", "1199606-0610")
conta = Conta(c1.get_nome(), 1222)

conta.deposito(100)
conta.saque(50)
conta.extrato()
```