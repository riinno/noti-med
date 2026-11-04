# Code by Riinno - Bruno Machado, 2026

# -----------------------------------------------------------------------------------
# Bibliotecas

import sqlite3
from pathlib import Path

# -----------------------------------------------------------------------------------
# Iniciando database

def connect_db():
  db_path = Path(__file__).resolve().parent.parent / "banco_artigos.db"

  conection = sqlite3.connect(db_path)
  return conection

# -----------------------------------------------------------------------------------
# Criando tabela no db

def create_table_db(conection: sqlite3.Connection):
  add_table = """
    CREATE TABLE IF NOT EXISTS articles (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      pmid INTEGER UNIQUE NOT NULL,
      title TEXT NOT NULL,
      pubdate TEXT NOT NULL
    )
  """
  
  conection.execute(add_table)
  conection.commit()

# -----------------------------------------------------------------------------------
# Criando novo Artigo no db

def create_many_articles(connection: sqlite3.Connection, article: tuple):
  insert_article = "INSERT INTO articles (pmid, title, pubdate) VALUES (?, ?, ?)"

  cursor = connection.cursor()
  cursor.executemany(insert_article, article)

# -----------------------------------------------------------------------------------
# Commitando mudancas no db

def commit_db(conection: sqlite3.Connection):
  conection.commit()

# -----------------------------------------------------------------------------------
# Fechando conexao com db

def close_connection_db(conection: sqlite3.Connection):
  conection.close()

# -----------------------------------------------------------------------------------