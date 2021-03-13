# connect_db.py
# import os
import sqlite3

''' A classe Connect representa o banco de dados. '''

class Connect(object):

    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo nome do banco
            print("Banco:", db_name)
            # lendo a versão do SQLite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            # imprimindo a versão do SQLite
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")

''' A classe ClientesDb representa um cliente no banco de dados. '''

class ClientesDb(object):

    def __init__(self):
        self.db = Connect('clientes.db')

    def close_connection(self):
        self.db.close_db()

if __name__ == '__main__':
    cliente = ClientesDb()
    cliente.close_connection()

# db = Connect('clientes.db')
# db.close_db()
# dir(Connect)
# db.__dict__