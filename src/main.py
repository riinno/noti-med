# Code by Riinno - Bruno Machado, 2026

# ------------------------------------------------------
# Bibliotecas

import requests
import dbartigos
import pubutils

# ------------------------------------------------------
# Faz a pesquisa na API do Eutils

etool_url, params = pubutils.api_eutils('esearch.fcgi?', 1)

response = requests.get(etool_url, params=params)
response_json = response.json()

print(response_json)
print(response_json["esearchresult"]["count"])

id_list = response_json["esearchresult"]["idlist"]

# ------------------------------------------------------
# Criando/Acessando banco de dados

# criando/acessando bd
conection = dbartigos.connect_db()

# criando tabela (se a tabela já existe, não cria)
dbartigos.create_table(conection)

conection.close()

# ------------------------------------------------------