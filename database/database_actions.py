import sys
from .pokemon import Pokemon
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

class DatabaseActions():
    logging.basicConfig(filename='logs/db.log',level=logging.DEBUG)

    def __init__(self):
        self.app = Flask(__name__)
        self.db = SQLAlchemy(self.app)


    def query_by_name(self, poke_name):
        """
        Add a poke to the database
        :param pokemon_name: string name of pokemon to get
        :rtype: Pokemon object
        """
        pokemon = self.db.session.query(Pokemon).filter(Pokemon.name == poke_name).first()
        if pokemon == None:
            logging.error('Requested DB query by name NOT found: ' + poke_name)
            return None, 404
        else:
            logging.info('Requested DB query by name found: ' + poke_name)
            return pokemon, 200


    def insert_poke_into_db(self, pokemon_id, name, pokemon_json):
        """
        Add a poke to the database

        :param pokemon_id: Pet to add to the store
        :param name: string name of the pokemon_name
        :param pokemon_json: raw json from pokemon web api
        :rtype: None
        """
        poke = Pokemon(pokemon_id, name, pokemon_json)
        if not self.query_by_name(name):
            self.db.session.add(poke)
            self.db.session.commit()
            logging.info('Inserted new pokemon into DB: ' + name)
        else:
            logging.info('Attempted pokemon insert already exists: ' + name)
        return {}, 201
