from flask_sqlalchemy import SQLAlchemy
from .pokemon import Pokemon
from flask import Flask
import logging

class DatabaseActions():
    logging.basicConfig(filename='logs/db.log',level=logging.DEBUG)

    def __init__(self):
        self.app = Flask(__name__)
        self.db = SQLAlchemy(self.app)


    def query_by_name(self, poke_name):
        """
        Add a poke to the database
        :param poke_name: string name of pokemon to get
        :rtype: Pokemon object, response code integer
        """
        pokemon = self.db.session.query(Pokemon).filter(Pokemon.name == poke_name).first()
        if pokemon == None:
            logging.error('Requested DB query by name NOT found: ' + poke_name)
            return None, 404
        else:
            logging.info('Requested DB query by name found: ' + poke_name)
            return pokemon, 200


    def query_by_id(self, poke_id):
        """
        Add a poke to the database
        :param poke_id: string id of pokemon to get
        :rtype: Pokemon object
        """
        pokemon = self.db.session.query(Pokemon).filter(Pokemon.pokemon_id == poke_id).first()
        if pokemon == None:
            logging.error('Requested DB query by id NOT found: ' + str(poke_id))
            return None, 404
        else:
            logging.info('Requested DB query by name found: ' + str(poke_id))
            return pokemon, 200


    def insert_poke_into_db(self, poke):
        """
        Add a poke to the database

        :param poke: Pokemon object
        :rtype: response code
        """
        _, response_code = self.query_by_name(poke.name)
        if response_code == 404:
            self.db.session.add(poke)
            self.db.session.commit()
            logging.info('Inserted new pokemon into DB: ' + poke.name)
        else:
            logging.info('Attempted pokemon insert already exists: ' + poke.name)
            return 418
        return 201
