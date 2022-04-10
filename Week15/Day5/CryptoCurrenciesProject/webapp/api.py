from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from webapp.config import Api

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': Api.CRYPTO_API
}


def get_active_cryptocurrency():
    """Returns id and names of active cryptocurrency."""
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return
    return [(coin["id"], coin["name"]) for coin in data["data"] if coin["is_active"]]


def get_cripto(search_id):
    """Receives a cryptocurrency by id from API."""

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return
    for coin in data["data"]:
        if coin["id"] == int(search_id):
            return coin
