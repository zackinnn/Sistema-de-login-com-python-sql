import sqlite3 

conn = sqlite3.connect('Users.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
      Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      Nome TEXT NOT NULL,
      Email TEXT NOT NULL,
      Usuario TEXT NOT NULL, 
      Senha TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")
