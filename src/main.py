# Code by Riinno - Bruno Machado, 2026

# -----------------------------------------------------------------------------------
# Bibliotecas

import requests
import dbartigos
import pubutils
from array import array

# -----------------------------------------------------------------------------------
# Faz a pesquisa na API do Eutils

search_url, params = pubutils.url_api_eutils(0,
                                            term='"digital health" AND wearable*')

response_search = requests.post(search_url, params=params)

print(response_search)

# salva os PMIDs que encontrou
id_array = array('q', map(int, response_search.json()["esearchresult"]["idlist"]))
# deleta a resposta da memoria, nao precisamos mais
del response_search

# -----------------------------------------------------------------------------------
# Procura resumos e titulos, e guarda no banco

# cria a request pra essumary
summary_url, params = pubutils.url_api_eutils(1, 
                                              array=id_array)

# para cada lote de PMIDs
for chunk in pubutils.split_chunks(id_array, 250):
  print(f"chunk_size: {len(chunk)}")
  for id in chunk:
    # procura os resumos de cada PMID
    # REQUEST ESSUMARY
    print("a")
    response_summary = requests.post(summary_url, params=params)
    

# -----------------------------------------------------------------------------------
# Criando/Acessando banco de dados

# criando/acessando bd
conection = dbartigos.connect_db()

# criando tabela (se a tabela já existe, não cria)
dbartigos.create_table(conection)

conection.close()

# -----------------------------------------------------------------------------------