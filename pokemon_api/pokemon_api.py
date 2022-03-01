from os import path
import requests
from flask_restful import Resource
import logging


class PokemonAPI(Resource):
    logging.basicConfig(filename='logs/pokemon_api.log',level=logging.DEBUG)

    def fetch_pokemon(value):
        url = path.join('https://pokeapi.co/api/v2/pokemon', value.lower())
        req = requests.get(url)
        try:
            poke = req.json()
            id = poke['id']
            name = poke['name']
            return id, name, poke

        except Exception as e:
            logging.error('Was not able to fetch from api')
            logging.error(e)
            return False, False, False
