# Code by Riinno - Bruno Machado, 2026

# ------------------------------------------------------
# Bibliotecas

import requests
import dbartigos
import pubutils

# -------------------------------------------------------------------------
# Faz a pesquisa na API do Eutils

search_url, params = pubutils.url_api_eutils('esearch.fcgi?', 1,
                                            'pubmed', 
                                            '"digital health" AND wearable*')

response = requests.get(search_url, params=params)
response_json = response.json()

print(response_json)
print(response_json["esearchresult"]["count"])

# salva os PMIDs que encontrou
id_array = response_json["esearchresult"]["idlist"]


# Procura os resumos de cada PMID
search_url, params = pubutils.url_api_eutils('', 0,
                                            'pubmed', 
                                            '"digital health" AND wearable*')

# -------------------------------------------------------------------------
# Criando/Acessando banco de dados

# criando/acessando bd
conection = dbartigos.connect_db()

# criando tabela (se a tabela já existe, não cria)
dbartigos.create_table(conection)

conection.close()

# -------------------------------------------------------------------------