# Code by Riinno - Bruno Machado, 2026

# -----------------------------------------------------------------------------------
# Bibliotecas

import sys
import requests
import db_interface
import pub_utils
from array import array

import time

# -----------------------------------------------------------------------------------
# Definicoes iniciais

# marca tempo
sys.stdout.reconfigure(encoding="utf-8")

# -----------------------------------------------------------------------------------
# AUXILIARES

# Gerar lista de tupla de artigos (devolve uma tupla por vez)
# tupla com (pmid, titulo, data de publicacao)
def gera_tupla_article(result_summary):
  for pmid, article in result_summary.items():
    yield (pmid, article["title"], article["pubdate"])

# -----------------------------------------------------------------------------------
# Faz a pesquisa de PMIDs na API do Eutils

inicio = time.perf_counter()

search_url, params = pub_utils.url_api_eutils(0, term='"digital health" AND wearable*')

response_search = requests.post(search_url, params=params)

# salva os PMIDs que encontrou
id_array = array('q', map(int, response_search.json()["esearchresult"]["idlist"]))

print(response_search.json()["esearchresult"]["count"])
# deleta a resposta da memoria, nao precisamos mais
del response_search

# -----------------------------------------------------------------------------------
# Criando/Acessando banco de dados

# criando/acessando bd
conection = db_interface.connect_db()

# criando tabela (se a tabela já existe, não cria)
db_interface.create_table_db(conection)

# -----------------------------------------------------------------------------------
# Procura resumos e titulos, e guarda no banco

# para cada lote de PMIDs
for chunk in pub_utils.split_chunks(id_array, 250):
  print(f"chunk_size: {len(chunk)}")

  # cria a request pra essumary, e salva a resposta da request
  summary_url, params = pub_utils.url_api_eutils(1, id_array=chunk)
  response_summary = requests.post(summary_url, params=params)
  
  # encontra ERROS DE REQUISICAO
  response_summary.raise_for_status()

  # salva o campo result
  result_summary = response_summary.json()["result"]
  # remove a lista de ids
  result_summary.pop("uids", None)

  # para cada pmid, busca infos dele e salva no bd
  db_interface.create_many_articles(conection, gera_tupla_article(result_summary))

  # commita a cada chunk
  db_interface.commit_db(conection)

print("")
print(response_summary.json())

print(result_summary)

del response_summary

# marca tempo
fim = time.perf_counter()
print(f"tempo para encontrar ids e buscar titulos: {fim - inicio:.2f} sec")

# -----------------------------------------------------------------------------------
# Fechando o db

db_interface.close_connection_db(conection)

# -----------------------------------------------------------------------------------