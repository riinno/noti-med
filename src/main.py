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
                                            'pubmed', 
                                            '"digital health" AND wearable*')

response = requests.get(search_url, params=params)

print(response)

# salva os PMIDs que encontrou
id_array = array('q', map(int, response.json()["esearchresult"]["idlist"]))
# deleta a resposta da memoria, nao precisamos mais
del response

# -----------------------------------------------------------------------------------
# Procura resumos e titulos, e guarda no banco

# para cada lote de PMIDs
# for lote in pubutils.split_chunks(id_array):
#   for id in lote:
#     # procura os resumos de cada PMID
#     summary_url, params = pubutils.url_api_eutils(1,
#                                                   'pubmed', 
#                                                   '"digital health" AND wearable*')

# -----------------------------------------------------------------------------------
# Criando/Acessando banco de dados

# criando/acessando bd
conection = dbartigos.connect_db()

# criando tabela (se a tabela já existe, não cria)
dbartigos.create_table(conection)

conection.close()

# -----------------------------------------------------------------------------------