from flask_restful import Resource
from database.pokemon import Pokemon
from os import path
import requests
import logging


class PokemonAPI(Resource):
    logging.basicConfig(filename='logs/pokemon_api.log',level=logging.DEBUG)

    def fetch_pokemon(in_value):
        """
        :param: in_value: string name or id
        :return: Pokemon object, respone code integer
        """
        url = path.join('https://pokeapi.co/api/v2/pokemon', in_value.lower())
        req = requests.get(url)
        try:
            poke_json = req.json()
            poke_id = poke_json['id']
            name = poke_json['name']
            poke = Pokemon(poke_id, name, poke_json)
            return poke, 200

        except Exception as e:
            logging.error('Was not able to fetch from api')
            logging.error(e)
            return None, 404
