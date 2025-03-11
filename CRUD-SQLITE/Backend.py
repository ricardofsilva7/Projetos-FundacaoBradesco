import sqlite3 as sql

class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql_query, parms=None):  # Correção de nome
        if TransactionObject.connected:
            if parms is None:
                TransactionObject.cur.execute(sql_query)
            else:
                TransactionObject.cur.execute(sql_query, parms)
            return True
        return False
        
    def fetchall(self):
        return TransactionObject.cur.fetchall()
    
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        return False
        
    @staticmethod
    def initDB():  # Tornando initDB um método estático
        trans = TransactionObject()
        trans.connect()
        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()    
        trans.disconnect()

    def insert(self, nome, sobrenome, email, cpf):
        self.connect()
        self.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        self.persist()
        self.disconnect()

    def view(self):
        self.connect()
        self.execute("SELECT * FROM clientes")
        rows = self.fetchall()
        self.disconnect()
        return rows
    
    def search(self, nome="", sobrenome="", email="", cpf=""):
        self.connect()
        self.execute("SELECT * FROM clientes WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))  
        rows = self.fetchall()
        self.disconnect() 
        return rows
    
    def delete(self, id):
        self.connect()
        self.execute("DELETE FROM clientes WHERE id = ?", (id,))
        self.persist()
        self.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        self.connect()
        self.execute("UPDATE clientes SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, id))
        self.persist()
        self.disconnect()

# Inicializa o banco de dados corretamente
TransactionObject.initDB()
