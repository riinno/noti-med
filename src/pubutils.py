# Code by Riinno - Bruno Machado, 2026

# ----------------------------------------------------------------------
# Bibliotecas

import requests

# ----------------------------------------------------------------------
# Constantes

# url do eutils (API PubMed)
URL_EUTILS = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

# ----------------------------------------------------------------------
# Monta o link para conectar com API eutils, de acordo com a ferramenta.
# Sempre JSON

# tool = ferramenta do eutils sendo utilizada
def url_api_eutils(tool: str, is_search: int, db: str, term: str):
  etool_url = f'{URL_EUTILS}{tool}'

  if is_search == 1:
    params = {
      "db": db,
      "term": term,
      "retmode": "json",

      # PENSAR NISSO AQUI
      # "retmax": 10000
    }
    
    return etool_url, params

  return etool_url

# ----------------------------------------------------------------------

def split_chunks():
  