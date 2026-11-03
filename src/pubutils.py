# Code by Riinno - Bruno Machado, 2026

# ----------------------------------------------------------------------
# Bibliotecas

import requests
from array import array

# ----------------------------------------------------------------------
# Constantes

# url do eutils (API PubMed)
URL_EUTILS = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

# ----------------------------------------------------------------------------
# Monta o link para conectar com API eutils, de acordo com a ferramenta.
# Sempre JSON

# tool = ferramenta do eutils sendo utilizada
def url_api_eutils(id_tool: int, first_param: str, sec_param: str, third_param):
  # decide qual ferramenta usar
  match id_tool:
    case 0:
      tool = 'esearch.fcgi?'
      params = {
        "db": first_param,
        "term": sec_param,
        "retmode": "json",

        # PENSAR NISSO AQUI
        "retmax": 10000
      }

    case 1:
      tool = 'esummary'
      params = {
        "db": first_param,
        "id": ",".join(third_param),
        "retmode": "json"
      }

  etool_url = f'{URL_EUTILS}{tool}'
  return etool_url, params

# ----------------------------------------------------------------------------
# Funcao que reparte uma informacao grande em "chunks",
# sendo essa informacao no formato de vetor.
# (generica, mas ate agora no main usamos apenas pra dividir a lista de PMIDs)

# jump = quantos elementos pegar para cada chunk
def split_chunks(array: array, jump: int):
  for i in range(0, len(array), jump):
    yield array[i:i + jump]

# ----------------------------------------------------------------------------