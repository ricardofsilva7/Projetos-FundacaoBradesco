
# **Projeto CRUD SQLite - PYSQL**

## **Descrição do Projeto**

O **PYSQL** é um projeto desenvolvido em **Python** utilizando a biblioteca **Tkinter** para criar uma interface gráfica para gerenciar um banco de dados SQLite. A aplicação permite ao usuário realizar operações de CRUD (Criar, Ler, Atualizar, Deletar) para gerenciar informações de clientes. A base de dados utilizada é um arquivo SQLite chamado `clientes.db`, onde são armazenados dados como nome, sobrenome, e-mail e CPF dos clientes.

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação utilizada.
- **Tkinter**: Biblioteca para criação de interfaces gráficas em Python.
- **SQLite**: Banco de dados utilizado para armazenamento de informações.
- **PyInstaller**: Ferramenta para gerar executáveis a partir do código Python.

## **Arquitetura do Projeto**

O projeto é composto por dois arquivos principais:

### **1. `Gui.py`**

Este arquivo contém a interface gráfica da aplicação, implementada com o Tkinter. A classe `Gui` define a janela principal da aplicação e os widgets necessários (como botões, campos de texto, e listas) para a interação do usuário.

- **Funções principais**:
  - `view_command()`: Exibe todos os registros de clientes no Listbox.
  - `search_command()`: Pesquisa clientes no banco de dados com base nos filtros de nome, sobrenome, e-mail e CPF.
  - `insert_command()`: Insere novos registros no banco de dados.
  - `update_command()`: Atualiza os dados de clientes existentes.
  - `del_command()`: Deleta os registros selecionados.

### **2. `Backend.py`**

Este arquivo contém a lógica de interação com o banco de dados SQLite. A classe `TransactionObject` gerencia a conexão com o banco de dados e fornece os métodos para realizar operações no banco, como inserir, atualizar, buscar, excluir e criar a tabela de clientes.

- **Funções principais**:
  - `initDB()`: Cria a tabela `clientes` no banco de dados, se não existir.
  - `insert(nome, sobrenome, email, cpf)`: Insere um novo cliente na tabela `clientes`.
  - `view()`: Retorna todos os registros de clientes.
  - `search(nome, sobrenome, email, cpf)`: Pesquisa clientes no banco de dados com base em um ou mais filtros.
  - `delete(id)`: Deleta um cliente da tabela com base no seu `id`.
  - `update(id, nome, sobrenome, email, cpf)`: Atualiza os dados de um cliente específico.

## **Fluxo do Aplicativo**

### **1. Inicialização**
- Ao iniciar o aplicativo, o método `initDB()` é chamado automaticamente para garantir que a tabela `clientes` exista no banco de dados. 

### **2. Operações CRUD**
- **Criar (Insert)**: O usuário pode inserir um novo cliente clicando no botão "Inserir". Os dados são coletados dos campos de texto e inseridos no banco de dados.
- **Ler (View)**: O botão "Ver todos" exibe todos os registros de clientes no Listbox.
- **Buscar (Search)**: O botão "Buscar" permite que o usuário pesquise clientes com base em filtros (nome, sobrenome, e-mail, CPF).
- **Atualizar (Update)**: O botão "Atualizar Selecionados" permite que o usuário edite as informações de um cliente selecionado.
- **Deletar (Delete)**: O botão "Deletar Selecionados" permite excluir um cliente selecionado da lista.

### **3. Interface Gráfica**
A interface gráfica foi desenvolvida utilizando Tkinter, e é composta por:
- **Campos de texto** para entrada de dados.
- **Botões** para executar ações como inserir, buscar, atualizar e deletar.
- **Listbox** para exibir os registros de clientes armazenados no banco de dados.
- **Scrollbar** associada ao Listbox para navegação quando a lista de clientes for extensa.

## **Comandos para Execução**

1. **Instalar dependências**:

   Certifique-se de ter o Python instalado em sua máquina. Instale as dependências necessárias (caso existam) com o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o Aplicativo**:

   Para rodar o aplicativo em ambiente local, basta executar o arquivo `Aplicacao.py`:

   ```bash
   python Aplicacao.py
   ```

3. **Gerar Executável**:

   Se deseja gerar um arquivo `.exe` para Windows, você pode utilizar o **PyInstaller**:

   ```bash
   pyinstaller --onefile --windowed --noconsole Application.py
   ```

## **Estrutura do Código**

### **`Gui.py`**

```python
# Código relacionado à interface gráfica utilizando Tkinter
from tkinter import *

class Gui:
    # Definições de widgets e funções da interface gráfica
    pass
```

### **`Backend.py`**

```python
# Código relacionado à interação com o banco de dados SQLite
import sqlite3 as sql

class TransactionObject:
    # Definição das funções para operações no banco de dados
    pass
```

## **Conclusão**

O **PYSQL** é uma aplicação simples para gerenciar dados de clientes utilizando SQLite. O projeto serve como um bom exemplo de como integrar a interface gráfica com operações de banco de dados, oferecendo funcionalidades essenciais de CRUD.

---