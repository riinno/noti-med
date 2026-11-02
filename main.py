# Code by Riinno - Bruno Machado, 2026

# ------------------------------------------------------
# Bibliotecas

import requests

# ------------------------------------------------------
# Montando o link para conectar com API eutils

# url do eutils
url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
# ferramenta do eutil, no caso esearch
tool = 'esearch.fcgi?'

search = f'{url}{tool}'

params = {
  "db": "pubmed",
  "term": '"digital health" AND wearable*',
  "retmode": "json",
  # "retmax": 4000
}

# ------------------------------------------------------
# Request e response

response = requests.get(search, params=params)
response_json = response.json()

print(response_json)
print(response_json["esearchresult"]["count"])

id_list = response_json["esearchresult"]["idlist"]

# ------------------------------------------------------