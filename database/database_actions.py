import sys
from .pokemon import Pokemon

class DatabaseActions():
    def __init__(self, db):
        self.db = db


    def query_by_name(self, name):
        pokemon = self.db.session.query(Pokemon).filter(Pokemon.name == name).first()
        if pokemon == None:
            pokemon = 'not found'
        return pokemon


    def insert_poke_into_db(self, pokemon_id, name, pokemon_json):
        poke = Pokemon(pokemon_id, name, pokemon_json)
        self.db.session.add(poke)
        self.db.session.commit()
