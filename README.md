# Descrição do Repositório

Este repositório contém três projetos desenvolvidos em Python, cada um abordando diferentes conceitos de desenvolvimento de software. Abaixo está uma breve descrição de cada projeto presente no repositório.

## 1. **Tela de Login com Kivy**

### Descrição
Este projeto implementa uma interface de login utilizando o framework **Kivy**. O sistema permite a criação de conta e autenticação de usuários, armazenando as informações em um arquivo de texto.

### Estrutura de Arquivos
```
.
├── main.py          # Lógica da interface gráfica
├── database.py      # Manipulação dos dados dos usuários
├── users.txt        # Armazena os usuários
└── my.kv            # Interface gráfica com Kivy
```

### Funcionalidades
- **Criação de conta** com validação de dados.
- **Autenticação de usuário** verificando email e senha.
- **Tela principal** exibindo informações do usuário após login.

### Melhorias Futuras
- Armazenamento de senhas com **criptografia**.
- Validação aprimorada de emails.
- Implementação de banco de dados SQL para persistência segura dos dados.

---

## 2. **PYSQL - CRUD com SQLite**

### Descrição
O **PYSQL** é um sistema de gerenciamento de clientes com interface gráfica, utilizando **Tkinter** e **SQLite**. O usuário pode realizar operações de **CRUD (Criar, Ler, Atualizar, Deletar)** em um banco de dados SQLite.

### Estrutura de Arquivos
```
.
├── Gui.py           # Interface gráfica com Tkinter
└── Backend.py       # Manipulação do banco de dados SQLite
```

### Funcionalidades
- **Cadastro** de clientes (Nome, Sobrenome, Email, CPF).
- **Consulta** de clientes com filtros.
- **Atualização** de dados de clientes.
- **Exclusão** de clientes.

### Melhorias Futuras
- Implementação de um sistema de autenticação.
- Exportação de dados para **CSV** ou **Excel**.
- Integração com banco de dados remoto.

---

## 3. **Sistema de Conta Bancária - POO em Python**

### Descrição
Projeto voltado para a prática de **Programação Orientada a Objetos (POO)** em Python. Implementa um sistema bancário simples com manipulação de contas e clientes.

### Estrutura de Arquivos
```
.
├── cliente.py       # Classe Cliente
└── conta.py         # Classe Conta
```

### Conceitos Utilizados
- **Encapsulamento** com métodos `get` e `set`.
- **Propriedades (`@property`)** para controle de saldo.
- **Operações bancárias** como saque, depósito e extrato.

### Melhorias Futuras
- Implementação de persistência de dados com banco de dados.
- Desenvolvimento de uma interface gráfica.
- Suporte a múltiplas contas por cliente.

---

## Como Executar os Projetos

### Requisitos
- Python 3.x instalado.
- Bibliotecas adicionais:
  ```bash
  pip install kivy sqlite3 tk
  ```

### Execução
Para cada projeto, navegue até o diretório correspondente e execute:
```bash
python main.py  # Para Tela de Login
python Gui.py   # Para PYSQL
python conta.py # Para Conta Bancária
```

---

## Conclusão
Este repositório é um conjunto de três projetos que exploram diferentes conceitos de desenvolvimento em Python, abordando interfaces gráficas, manipulação de bancos de dados e programação orientada a objetos. Cada projeto pode ser expandido e aprimorado para atender a novos desafios e necessidades.
