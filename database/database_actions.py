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


    def query_by_name(self, name):

        pokemon = self.db.session.query(Pokemon).filter(Pokemon.name == name).first()
        if pokemon == None:
            logging.error('Requested DB query by name NOT found: ' + name)
            pokemon = False
        else:
            logging.info('Requested DB query by name found: ' + name)
        return pokemon


    def insert_poke_into_db(self, pokemon_id, name, pokemon_json):
        # TODO: check if already in DB before inserting
        poke = Pokemon(pokemon_id, name, pokemon_json)
        if not self.query_by_name(name):
            self.db.session.add(poke)
            self.db.session.commit()
            logging.info('Inserted new pokemon into DB: ' + name)
        else:
            logging.info('Attempted pokemon insert already exists: ' + name)
