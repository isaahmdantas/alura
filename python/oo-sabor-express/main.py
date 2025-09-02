from typing import Dict, List, Optional, Tuple, Any
import logging
import requests
from fastapi import FastAPI, Query 

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    '''
        Endpoint que exibe uma mensagem incrivel  do mundo da programação.
    '''
    return {'Hello': 'World'}

import logging

logging.basicConfig(level=logging.INFO)

def fetch_restaurant_data(url: str = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json') -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
    logging.info(f"Fetching restaurant data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"Successfully fetched restaurant data from {url}")
        return response.json(), None
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching restaurant data from {url}: {e}")
        return None, str(e)

@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: Optional[str] = Query(None)) -> Dict[str, Any]:
    '''
        Endpoint para ver os cardápios dos restaurantes
    '''
    logging.info(f"Getting restaurants with restaurante: {restaurante}")
    dados_json, error = fetch_restaurant_data()
    if error:
        return {'Erro': error}

    if restaurante is None:
        return {'Dados': dados_json}

    dados_restaurante = []
    for item in dados_json:
        if item['Company'] == restaurante:
            dados_restaurante.append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })
    if not dados_restaurante:
        return {'Erro': f"Restaurante '{restaurante}' não encontrado."}
    return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}

