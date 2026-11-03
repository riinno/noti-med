# Code by Riinno - Bruno Machado, 2026

# -----------------------------------------------------------------------------------
# Bibliotecas

import sqlite3
from pathlib import Path

# -----------------------------------------------------------------------------------
# Iniciando database

def connect_db ():
  db_path = Path(__file__).resolve().parent.parent / "banco_artigos.db"

  conection = sqlite3.connect(db_path)
  return conection

# -----------------------------------------------------------------------------------
# Criando tabela no db

def create_table(conection: sqlite3.Connection):
  add_table = """
    CREATE TABLE IF NOT EXISTS artigos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      pmid INTEGER UNIQUE NOT NULL,
      title TEXT
    )
  """
  
  conection.execute(add_table)
  conection.commit()

# -----------------------------------------------------------------------------------
# Criando novo Artigo no db

def create_artigo():
  return

# -----------------------------------------------------------------------------------