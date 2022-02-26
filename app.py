# app.py - a minimal flask api using flask_restful
from flask import Flask, jsonify
from flask_restful import Resource, Api
import requests
import json

# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.dialects.postgresql import JSON

# from sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)
#                                                     username:pw                  db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@172.17.0.2:5432/docker'
db = SQLAlchemy(app)
# api = Api(app)


class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    pokemon_id = db.Column(db.String, primary_key=True, nullable=False)
    # for some reason JSONB is not supported? would be faster for queries.
    poke_json = db.Column(db.JSON, nullable=False)


    def __init__(self, id, json_string):
        self.pokemon_id = id
        self.poke_json = json_string



class PokemonAPI(Resource):
    def fetch_pokemon():
        url = 'https://pokeapi.co/api/v2/pokemon/1'
        req = requests.get(url)
        pokes = req.json()
        return 1, pokes


    def insert_poke(pokemon_id, pokemon_json):
        poke = Pokemon(pokemon_id, pokemon_json)
        db.session.add(poke)
        db.session.commit()

# from models import Result

#
@app.route('/')
def hello():
    return "Hello World!"
#
#
@app.route('/balb')
def fetch_balb():
    poke_id, poke_json = PokemonAPI.fetch_pokemon()
    PokemonAPI.insert_poke(poke_id, poke_json)
    # print(pokemon_json['name'])
    return "Hello {}!".format(poke_json)

# api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
