import datetime
import os

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        # Verifica se o arquivo existe. Se não, cria um novo
        if not os.path.exists(self.filename):
            print(f"Arquivo {self.filename} não encontrado. Criando um novo arquivo.")
            with open(self.filename, "w") as f:
                f.write("")  # Cria o arquivo vazio, pois o arquivo precisa existir
            self.users = {}
        else:
            # Se o arquivo já existe, lê os dados
            self.file = open(self.filename, "r")
            self.users = {}
            for line in self.file:
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)
            self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email já existe.")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
