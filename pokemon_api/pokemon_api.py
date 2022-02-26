from os import path
import requests
from flask_restful import Resource

class PokemonAPI(Resource):
    def fetch_pokemon(value):
        url = path.join('https://pokeapi.co/api/v2/pokemon', value)
        req = requests.get(url)
        poke = req.json()
        id = poke['id']
        name = poke['name']
        return id, name, poke
