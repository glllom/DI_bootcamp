import requests
import os
import json
dirname = os.path.dirname(__file__)


def get_all_pokemons():
    all_pokemons = []
    for pokemon in requests.get("https://pokeapi.co/api/v2/pokemon?limit=500&offset=0").json()["results"]:
        response = requests.get(pokemon["url"]).json()
        pokemon_dict = {"id": response["id"], "name": response["name"],
                        "type": [pokemon_type['type']['name'] for pokemon_type in response['types']],
                        "base_price": response["stats"][0]["base_stat"]}
        url = response["sprites"]["other"]["official-artwork"]["front_default"]
        download_image(url, f"{response['id']}.png")
        all_pokemons.append(pokemon_dict)
    with open(f"{dirname}/static/data/all_pokemons.json", 'w') as f:
        json.dump(all_pokemons, f, indent=4)


def download_image(url, filename):
    with open(f"{dirname}/static/img/pokemons/{filename}", 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)





