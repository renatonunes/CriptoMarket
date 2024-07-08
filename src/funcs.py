import requests
import json



def get_collection(collection, apikey_opensea):

    url_get_collection = f"https://api.opensea.io/api/v2/collections/{collection}"

    headers = {
        "accept": "application/json",
        "x-api-key": f"{apikey_opensea}"
    }
    response = json.loads(requests.get(url_get_collection, headers=headers).text)

    colecao = response["collection"]
    nome = response["name"]
    imagem = response["image_url"]
    data_criacao = response["created_date"]

    return {
        "nome":nome,
        "colecao":colecao,
        "imagem":imagem,
        "data_criacao":data_criacao
    }

