from flask_restful import Resource
from database.pokemon import Pokemon
from os import path
import requests
import logging


class PokemonAPI(Resource):
    logging.basicConfig(filename='logs/pokemon_api.log',level=logging.DEBUG)

    def fetch_pokemon(value):
        url = path.join('https://pokeapi.co/api/v2/pokemon', value.lower())
        req = requests.get(url)
        try:
            poke_json = req.json()
            id = poke_json['id']
            name = poke_json['name']
            poke = Pokemon(id, name, poke_json)
            return poke, 200

        except Exception as e:
            logging.error('Was not able to fetch from api')
            logging.error(e)
            return None, 404
