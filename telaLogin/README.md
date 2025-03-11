
# Projeto Tela de Login com Kivy

Aplicação simples de login e criação de conta com Kivy. Utiliza um arquivo de texto (`users.txt`) para armazenar as informações de usuários.

## Estrutura de Arquivos

```
.
├── main.py          # Lógica da interface gráfica
├── database.py      # Manipulação dos dados dos usuários
└── users.txt        # Armazena os usuários
└── my.kv            # Interface gráfica com Kivy
```

## Arquivo `main.py`

### Funções principais:

- **CreateAccountWindow**: Tela para criar uma nova conta.
- **LoginWindow**: Tela de login.
- **MainWindow**: Tela principal após login, mostrando as informações do usuário.
- **WindowManager**: Gerencia a navegação entre telas.

### Navegação:

1. **Criar conta**: Valida dados e cria um novo usuário no `users.txt`.
2. **Login**: Verifica se o email e senha correspondem a um usuário. Se sim, redireciona para a tela principal.
3. **Tela Principal**: Exibe nome, email e data de criação do usuário.

## Arquivo `database.py`

### Funcionalidades:

- **load()**: Carrega os usuários do arquivo `users.txt`.
- **add_user()**: Adiciona um novo usuário ao arquivo.
- **validate()**: Verifica se o email e senha correspondem a um usuário.
- **save()**: Salva as alterações de usuários no `users.txt`.
- **get_date()**: Retorna a data atual (sem hora).

### Estrutura do Arquivo `users.txt`:

```
email;senha;nome;data_de_criacao
```

Exemplo:
```
usuario1@example.com;senha123;João Silva;2025-03-01
```

## Como Rodar

1. Instale o Python 3.x e o Kivy.
2. Execute `main.py`:
   ```
   python main.py
   ```

## Melhorias Possíveis

- **Criptografia de Senhas**: Utilizar hash para armazenar senhas de forma segura.
- **Validação de Email**: Melhorar a validação do formato de email.
- **Backup de Dados**: Criar backups automáticos do `users.txt`.

## Conclusão

Esse projeto é uma implementação simples de login e cadastro usando Kivy e um arquivo de texto para persistência dos dados. Pode ser expandido com novas funcionalidades e melhorias de segurança.
```